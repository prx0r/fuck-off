from CoreNanopub.utils import _extractSentenceID, _extractGCSID
from extended_nanopub import ExtendedNanopub
from rdflib import URIRef, Literal
from rdflib.namespace import DCTERMS, XSD, RDFS, RDF
from datetime import datetime

assigned_certainty_degree = {"ONCOGENE": "AGTOncogeneLikelihood",
                             "BIOMARKER": "EGRPassiveLikelihood",
                             "TSG": "AGTTSGLikelihood"}
assigned_certainty_degree_support = {"ONCOGENE": "AGTOncogeneSupport",
                                     "BIOMARKER": "EGRPassiveSupport",
                                     "TSG": "AGTTSGSupport"}


def _createNanopub(self, gcs_row):
    """

    :param gcs_row: (pandas.Series) row comprise the fact's information.
    :return:
    """
    self.logger.info(f"+++ Creating nanopublication {gcs_row.name} ({self.current_serialized}/{self.to_be_serialized})")
    self.current_serialized += 1
    self.initializeFullGraph(gcs_row.name)

    self.initializeNanopubGraphs()

    self._populateAssertionGraph(gcs_row),
    self._populateProvenanceGraph(),
    self._populatePubInfoGraph(gcs_row),
    self._populateKnowledgeProvGraph(gcs_row)

    np = ExtendedNanopub(rdf=self.nanopub_graph)
    self.logger.info(f"Serializing nanopublication {gcs_row.name}")
    for ser_format in self.serialization_formats:
        np._rdf.serialize(self.serialization_path[ser_format] + f"{gcs_row.name}.{ser_format}", format=ser_format)
        self.logger.info(f"+++ Nanopublication saved at {self.serialization_path[ser_format]}{gcs_row.name}.{ser_format}")
    return None


def _populateAssertionGraph(self, gcs_row):
    """
    Populates the assertion graph for the extended_nanopub of the considered GCS.

    :param self: self object.
    :param gcs_row: (pandas.Series) row with GCS information.
    """
    # Add GCS
    self.assertion_graph.add((URIRef(gcs_row["gcs_uri"]), RDF.type, self.namespaces["ceonto"]["GCS"]))
    # Add involved disease
    self.assertion_graph.add((URIRef(gcs_row["gcs_uri"]), self.namespaces["ceonto"]["involves"],
                              URIRef(gcs_row["involves"])))
    # Add involved gene
    self.assertion_graph.add((URIRef(gcs_row["gcs_uri"]), self.namespaces["ceonto"]["expressedBy"],
                              URIRef(gcs_row["expressedBy"])))
    # Add gene's class
    self.assertion_graph.add((URIRef(gcs_row["gcs_uri"]), self.namespaces["ceonto"]["hasType"],
                              Literal(gcs_row["hasType"], datatype=XSD.string)))


def _populatePubInfoGraph(self, gcs_row):
    """
    Populates the publication info graph for the extended_nanopub of the considered GCS.

    :param self: self object.
    :param gcs_row: (pandas.Series) row with GCS information.
    """
    # Add created timestamp
    self.pubinfo_graph.add((self.nanopub_graph.identifier, DCTERMS.created,
                            Literal(datetime.now(), datatype=XSD.dateTime)))
    # Add creator
    self.pubinfo_graph.add((self.nanopub_graph.identifier, DCTERMS.creator,
                            URIRef(self.namespaces["orcid"]["0000-0002-0676-682X"])))
    # Add authors
    self.pubinfo_graph.add((self.nanopub_graph.identifier, self.namespaces["pav"]["authoredBy"],
                            URIRef(self.namespaces["orcid"]["0000-0002-0676-682X"])))
    self.pubinfo_graph.add((self.nanopub_graph.identifier, self.namespaces["pav"]["authoredBy"],
                            URIRef(self.namespaces["orcid"]["0000-0003-0362-5893"])))
    self.pubinfo_graph.add((self.nanopub_graph.identifier, self.namespaces["pav"]["authoredBy"],
                            URIRef(self.namespaces["orcid"]["0000-0003-4970-4554"])))
    self.pubinfo_graph.add((self.nanopub_graph.identifier, self.namespaces["pav"]["authoredBy"],
                            URIRef(self.namespaces["orcid"]["0000-0001-5015-5498"])))
    self.pubinfo_graph.add((self.nanopub_graph.identifier, self.namespaces["pav"]["authoredBy"],
                            URIRef(self.namespaces["orcid"]["00009-0009-2515-4771"])))
    # Add license
    self.pubinfo_graph.add((self.nanopub_graph.identifier, DCTERMS.rights,
                            URIRef("http://opendatacommons.org/licenses/odbl/1.0/")))
    # Add subject (Gene-Disease Associations)
    self.pubinfo_graph.add((self.nanopub_graph.identifier, DCTERMS.subject,
                            URIRef(self.namespaces["SIO"]["001123"])))

    if gcs_row["hasType"] != "UNCERTAIN":
        # Add reference to the RDF dataset
        self.pubinfo_graph.add((self.nanopub_graph.identifier, self.namespaces["prv"]["usedData"],
                                URIRef("https://doi.org/10.5281/zenodo.7577127")))
        self.pubinfo_graph.add((URIRef("https://doi.org/10.5281/zenodo.7577127"), self.namespaces["pav"]["version"],
                                Literal("v1.1", datatype=XSD.string)))


def _populateProvenanceGraph(self):
    """
    Populates the provenance graph for the extended_nanopub of the considered GCS.

    :param self: self object.
    """
    # Add Activity
    self.provenance_graph.add((self.assertion_graph.identifier, self.namespaces["prov"]["wasGeneratedBy"],
                              self.namespaces["ECO"]["0000203"]))
    # Add Entity
    self.provenance_graph.add((self.assertion_graph.identifier, self.namespaces["prov"]["wasDerivedFrom"],
                              URIRef("https://gda.dei.unipd.it/")))
    # Link Evidence to the assertion
    self.provenance_graph.add((self.assertion_graph.identifier, self.namespaces["wi"]["evidence"],
                               self.namespaces["ceonto"]["gcsEvidence"]))
    # Instantiate Evidence
    self.provenance_graph.add((self.namespaces["ceonto"]["gcsEvidence"], RDF.type,
                              self.namespaces["ECO"]["0000212"]))
    self.provenance_graph.add((self.namespaces["ceonto"]["gcsEvidence"], RDFS.label,
                              Literal("CORE Gene Cancer Status (GCS)", lang="en")))
    self.provenance_graph.add((self.namespaces["ceonto"]["gcsEvidence"], RDFS.comment,
                              Literal("Gene expression-cancer association harvested from collecting the scientific"
                                      " literature from different sources.", lang="en")))


def _populateKnowledgeProvGraph(self, gcs_row):
    """
    Populates the knowledge provenance graph for the extended_nanopub of the considered GCS.

    :param self: self object.
    :param gcs_row: (pandas.Series) row with GCS information.
    """
    # Add supporting or contrasting sentences
    restricted_df = self.gcs_sentence.loc[self.gcs_sentence["gcs"] == gcs_row["gcs_uri"]]
    restricted_df.apply(self._insertEvidence, axis=1)
    # Link assertion to the assigned truth value
    self.knowledgeprov_graph.add((self.assertion_graph.identifier,
                                  self.namespaces["PROV-K"]["hasTruthValue"],
                                  self.namespaces["corekp"][f"{gcs_row.name}"]))
    # Add Truth Value
    if gcs_row["hasType"] == "UNCERTAIN":
        self.logger.info(f"Nanopub {gcs_row.name} is an UNCERTAIN fact")
        # Add unreliable fact
        # Check if the fact failed the sufficiency check
        if gcs_row["CCSNotInformativeLikelihood"] > 0.7:
            # CCS failed the sufficiency check
            # Add insufficient evidence fact
            self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                         RDF.type, self.namespaces["PROV-K"]["InsufficientEvidence"]))
            # Add unreliability reason
            if gcs_row["PTNotInformativeLikelihood"] > 0.7:
                self.logger.info(f"Nanopub {gcs_row.name} is uncertain due to insufficient evidence for CCS and GCI")
                # Both CCS and CGI failed the sufficiency check
                self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                             self.namespaces["PROV-K"]["unreliabilityReason"],
                                             Literal("Insufficient evidence for determining the Change of Cancer Status"
                                                     " (CCS) and the Gene-Cancer Interaction (GCI).",
                                                     datatype=XSD.string)))
                self._insertSufficiencyCondition(gcs_row.name, gcs_row["CCSNotInformativeLikelihood"],
                                                 "ccsCriteria")
                self._insertSufficiencyCondition(gcs_row.name, gcs_row["PTNotInformativeLikelihood"],
                                                 "gciCriteria")
            else:
                self.logger.info(f"Nanopub {gcs_row.name} is uncertain due to insufficient evidence for CCS")
                # CCS failed the sufficiency check
                self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                             self.namespaces["PROV-K"]["unreliabilityReason"],
                                             Literal("Insufficient evidence for determining the the Change of Cancer "
                                                     "Status (CCS)", datatype=XSD.string)))
                self._insertSufficiencyCondition(gcs_row.name, gcs_row["CCSNotInformativeLikelihood"],
                                                 "ccsCriteria")
        elif gcs_row["PTNotInformativeLikelihood"] > 0.7:
            self.logger.info(f"Nanopub {gcs_row.name} is uncertain due to insufficient evidence for GCI")
            # CGI failed the sufficiency check
            # Add insufficient evidence fact
            self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                         RDF.type, self.namespaces["PROV-K"]["InsufficientEvidence"]))
            self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                         self.namespaces["PROV-K"]["unreliabilityReason"],
                                         Literal("Insufficient evidence for determining the Gene-Cancer Interaction"
                                                 " (GCI).", datatype=XSD.string)))
            self._insertSufficiencyCondition(gcs_row.name, gcs_row["PTNotInformativeLikelihood"],
                                             "gciCriteria")
        elif abs(gcs_row["EGRActiveLikelihood"]-gcs_row["EGRPassiveLikelihood"]) <= 0.4:
            self.logger.info(f"Nanopub {gcs_row.name} is uncertain due to contrasting evidence for active (oncogene,"
                                f" or tumor supressor gene) or passive (biomarker) role.")
            # Active and Passive gene role failed the consistency check
            # Add inconsistency evidence fact
            self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                         RDF.type, self.namespaces["PROV-K"]["ContrastingEvidence"]))
            self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                         self.namespaces["PROV-K"]["unreliabilityReason"],
                                         Literal("Contrasting evidence for determining an active (oncogene, or tumor "
                                                 "supressor gene) or passive (biomarker) role.", datatype=XSD.string)))
            self._insertConsistencyCondition(gcs_row.name,
                                             abs(gcs_row["EGRActiveLikelihood"]-gcs_row["EGRPassiveLikelihood"]))
        elif gcs_row["EGRPassiveLikelihood"] > gcs_row["EGRActiveLikelihood"]:
            raise ValueError(f"GCS {gcs_row.name} deemed as \"UNRELIABLE\" but should be \"BIOMARKER\"")
        else:
            self.logger.info(f"Nanopub {gcs_row.name} is uncertain due to contrasting evidence for oncogene or tumor"
                             f" suppressor gene.")
            if abs(gcs_row["AGTOncogeneLikelihood"]-gcs_row["AGTTSGLikelihood"]) <= 0.4:
                # oncogene and tumor supressor gene failed the consistency check
                # Add inconsistency evidence fact
                self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                             RDF.type, self.namespaces["PROV-K"]["ContrastingEvidence"]))
                self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                             self.namespaces["PROV-K"]["unreliabilityReason"],
                                             Literal("Contrasting evidence for determining oncogene or tumor suppressor"
                                                     " gene's role.", datatype=XSD.string)))
                self._insertConsistencyCondition(gcs_row.name,
                                                 abs(gcs_row["AGTOncogeneLikelihood"] - gcs_row["AGTTSGLikelihood"]))
            else:
                raise ValueError(f"GCS {gcs_row.name} deemed as \"UNRELIABLE\" but should be either \"ONCOGENE\" or"
                                 f" \"TSG\"")
    else:
        self.logger.info(f"Nanopub {gcs_row.name} is a RELIABLE fact")
        # Add reliable fact
        self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                     RDF.type, self.namespaces["PROV-K"]["ReliableFact"]))
        # Add assigned certainty degree
        self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                     self.namespaces["PROV-K"]["assignedCertaintyDegree"],
                                     Literal(gcs_row[assigned_certainty_degree[gcs_row["hasType"]]],
                                             datatype=XSD.float)))
        # Add assigned certainty support
        self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_row.name}"],
                                     self.namespaces["PROV-K"]["assignedCertaintyDegreeSupport"],
                                     Literal(gcs_row[assigned_certainty_degree_support[gcs_row["hasType"]]],
                                             datatype=XSD.integer)))


def _insertEvidence(self, gcs_sentence_row):
    """
    Insert conflicting and supporting sentence for the considered GCS.

    :param self: self object.
    :param gcs_sentence_row (panda.Series): series representing a row containing information and GCS and a sentence.
    """
    if isinstance(gcs_sentence_row["sentenceClass"], str):
        # sentence is informative
        if gcs_sentence_row["sentenceClass"] == gcs_sentence_row["gcsClass"]:
            # add supporting sentence
            self.knowledgeprov_graph.add((self.assertion_graph.identifier,
                                          self.namespaces["PROV-K"]["supportedBy"],
                                          URIRef(gcs_sentence_row["sentence"])))
        else:
            # add conflicting sentence
            self.knowledgeprov_graph.add((self.assertion_graph.identifier,
                                         self.namespaces["PROV-K"]["conflictingWith"],
                                         URIRef(gcs_sentence_row["sentence"])))
    else:
        # sentence is not informative, do not insert it
        sentence_id = _extractSentenceID(gcs_sentence_row["sentence"])
        gcs_id = _extractGCSID(gcs_sentence_row["gcs"])
        self.logger.warning(f"Sentence {sentence_id} is not informative for GCS {gcs_id} -- discarded")


def _insertSufficiencyCondition(self, gcs_id, sufficiency_score, sufficiency_class):
    """
    Insert information about the specific sufficiency check.

    :param self: self object.
    :param gcs_id: (str) ID of the considered GCS.
    :param sufficiency_score: (float) Sufficiency score of the considered aspect.
    :param sufficiency_class: (str) Aspect which failed the sufficiency check.
    """
    # Instantiate the sufficiency score
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}#{sufficiency_class}"],
                                 RDF.type, self.namespaces["PROV-K"][sufficiency_class]))
    # Link the sufficiency score to the truth value
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}"],
                                 self.namespaces["PROV-K"]["unmetCondition"],
                                 self.namespaces["corekp"][f"{gcs_id}#{sufficiency_class}"]))
    # Add threshold
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}#{sufficiency_class}"],
                                 self.namespaces["PROV-K"]["conditionThreshold"],
                                 Literal(0.7, datatype=XSD.float)))
    # Add score
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}#{sufficiency_class}"],
                                 self.namespaces["PROV-K"]["conditionScore"],
                                 Literal(sufficiency_score, datatype=XSD.float)))
    # Add criteria
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}#{sufficiency_class}"],
                                  self.namespaces["PROV-K"]["conditionCriteria"],
                                  self.namespaces["ceonto"][sufficiency_class]))


def _insertConsistencyCondition(self, gcs_id, consistency_score):
    """
    Insert information about the specific consistency check.

    :param self: self object.
    :param gcs_id: (str) ID of the considered GCS.
    :param consistency_score: (float) Consistency score of the considered aspect.
    """
    # Instantiate the sufficiency score
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}#geneClassCriteria"],
                                 RDF.type, self.namespaces["PROV-K"]["ConsistencyScore"]))
    # Link the sufficiency score to the truth value
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}"],
                                 self.namespaces["PROV-K"]["unmetCondition"],
                                 self.namespaces["corekp"][f"{gcs_id}#geneClassCriteria"]))
    # Add threshold
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}#geneClassCriteria"],
                                 self.namespaces["PROV-K"]["consistencyThreshold"],
                                 Literal(0.4, datatype=XSD.float)))
    # Add score
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}#geneClassCriteria"],
                                 self.namespaces["PROV-K"]["consistencyScore"],
                                 Literal(consistency_score, datatype=XSD.float)))
    # Add criteria
    self.knowledgeprov_graph.add((self.namespaces["corekp"][f"{gcs_id}#geneClassCriteria"],
                                  self.namespaces["PROV-K"]["conditionCriteria"],
                                  self.namespaces["ceonto"]["geneClassCriteria"]))
