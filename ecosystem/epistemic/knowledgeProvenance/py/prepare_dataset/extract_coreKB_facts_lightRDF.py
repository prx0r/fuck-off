import re

import rdflib
from collections import defaultdict
import pandas as pd
import lightrdf
from lightrdf.python_module.parse import literal, iri

CEONTO = "<http://gda.dei.unipd.it/cecore/ontology/"
SIO = "<http://semanticscience.org/resource/SIO_"
RDF = "<http://www.w3.org/1999/02/22-rdf-syntax-ns#"


def extract_facts(dump, logger):
    logger.info(f"...Iterating over the facts")
    # convert output to DataFrame
    gcs_dict = defaultdict(list)
    gcs_sentence_dict = defaultdict(list)
    count = 1
    for triple in dump.search_triples(None, RDF+'type>', CEONTO+'GCS>'):
        gcs_id = re.sub("http://gda.dei.unipd.it/cecore/resource/GCS#", "", triple[0])
        logger.info(f"...Considering GCS {gcs_id} ({count}/231099)")
        logger.info(f"GCS URI: {triple[0]}")
        count += 1
        # store gcs URI
        gcs_dict['id'].append(iri(triple[0]))
        # store additional information associated w/ GCS
        logger.info(f"Extracting GCS information...")
        # involved disease
        involves_triple = list(dump.search_triples(triple[0], CEONTO+"involves>", None))[0]
        # gene class
        hasType_triple = list(dump.search_triples(triple[0], CEONTO + "hasType>", None))[0]
        # gene expression
        expressedBy_triple = list(dump.search_triples(triple[0], CEONTO + "expressedBy>", None))[0]
        # Probabilities
        CCSnotInf_triple = list(dump.search_triples(triple[0], CEONTO+"CCSNotInformativeLikelihood>", None))[0]
        PTnotInf_triple = list(dump.search_triples(triple[0], CEONTO+"PTNotInformativeLikelihood>", None))[0]
        EGRActive_triple = list(dump.search_triples(triple[0], CEONTO+"EGRActiveLikelihood>", None))[0]
        EGRPassive_triple = list(dump.search_triples(triple[0], CEONTO+"EGRPassiveLikelihood>", None))[0]
        AGTOncog_triple = list(dump.search_triples(triple[0], CEONTO+"AGTOncogeneLikelihood>", None))[0]
        AGTTSG_triple = list(dump.search_triples(triple[0], CEONTO+"AGTTSGLikelihood>", None))[0]
        # Store GCS information in dictionary
        gcs_dict['involves'].append(iri(involves_triple[2]))
        gcs_dict['hasType'].append(literal(hasType_triple[2])[0])
        gcs_dict['expressedBy'].append(iri(expressedBy_triple[2]))
        gcs_dict['CCSNotInformativeLikelihood'].append(literal(CCSnotInf_triple[2])[0])
        gcs_dict['PTNotInformativeLikelihood'].append(literal(PTnotInf_triple[2])[0])
        gcs_dict['EGRActiveLikelihood'].append(literal(EGRActive_triple[2])[0])
        gcs_dict['EGRPassiveLikelihood'].append(literal(EGRPassive_triple[2])[0])
        gcs_dict['AGTOncogeneLikelihood'].append(literal(AGTOncog_triple[2])[0])
        gcs_dict['AGTTSGLikelihood'].append(literal(AGTTSG_triple[2])[0])
        # Extract related sentences
        extract_gcs_sentence(dump, gcs_sentence_dict, logger, str(triple[0]))
        logger.info(f"+++ GCS {gcs_id} COMPLETED +++")
    gcs = pd.DataFrame(gcs_dict)
    gcs_sentence = pd.DataFrame(gcs_sentence_dict)
    return gcs, gcs_sentence


def extract_gene_class(dump, sentence_uri):
    # classify the sentence
    PTLabel = literal(list(dump.search_triples(sentence_uri, CEONTO + 'PTLabel>', None))[0][2])[0]
    CCSLabel = literal(list(dump.search_triples(sentence_uri, CEONTO + 'CCSLabel>', None))[0][2])[0]
    CGELabel = literal(list(dump.search_triples(sentence_uri, CEONTO + 'CGELabel>', None))[0][2])[0]
    if PTLabel != 'NOTINF':
        # update EGR
        if PTLabel == 'OBSERVATION':
            # sentence supports a passive role for target gene (i.e., BIOMARKER)
            return "BIOMARKER"

    if PTLabel == 'CAUSALITY' and CCSLabel != 'NOTINF':
        # sentence supports an active role for target gene
        if (CGELabel == 'UP' and CCSLabel == 'PROGRESSION') or \
                (CGELabel == 'DOWN' and CCSLabel == 'REGRESSION'):
            # ONCOGENE
            return "ONCOGENE"
        if (CGELabel == 'DOWN' and CCSLabel == 'PROGRESSION') or \
                (CGELabel == 'UP' and CCSLabel == 'REGRESSION'):
            # TSG
            return "TSG"
    return None


def extract_gcs_sentence(dump, gcs_sentence_dict, logger, gcs_uri):
    logger.info(f".....Extracting related sentences")
    # convert query output to DataFrame
    triples = list(dump.search_triples(gcs_uri, CEONTO + 'supportedBy>', None))
    num_triples = len(triples)
    logger.info(f"Found {num_triples} related sentences")
    count = 1
    for triple in triples:
        logger.info(f"Considering sentence # {count} of {num_triples}")
        count += 1
        # store gcs URI
        gcs_sentence_dict['gcs'].append(iri(gcs_uri))
        # store sentence associated w/ GCS
        gcs_sentence_dict['sentence'].append(iri(triple[2]))
        logger.info(f"Extracting gene class for sentence {triple[2]}...")
        gcs_sentence_dict['sentenceClass'].append(extract_gene_class(dump, triple[2]))

    return None

