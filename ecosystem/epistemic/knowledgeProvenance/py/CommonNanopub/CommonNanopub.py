from Logger import DebugLogger
import configparser
from rdflib import Namespace, ConjunctiveGraph, Graph
from rdflib.namespace import DC, DCTERMS, FOAF, XSD, RDFS, RDF

from extended_nanopub.namespaces import NP


class CommonNanopub:

    def __init__(self, path_to_properties='../properties/common.ini'):
        """
        Initialisation function.

        :param path_to_properties : (str) path to properties file.
        """
        self.logger = DebugLogger().logger

        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.config.read(path_to_properties)

        # Data directory path
        self.datadir = self.config['PATHS']['datadir']
        self.ontoPath = self.datadir + self.config["PATHS.ONTOLOGY"]["ontology"]

    def get_namespaces(self, nanopub_id):
        """
        Create a dictionary with ('namespace_id', URL) of each namespace defined in the classification class.
        """
        self.namespaces = {nid: Namespace(uri) for nid, uri in self.config['NAMESPACES'].items()}
        self.namespaces["this"] = Namespace(self.namespaces["npuri"] + nanopub_id)
        self.namespaces["sub"] = Namespace(self.namespaces["npuri"] + nanopub_id + "#")

    def read_data(self):
        """
        Read the facts to be published as nanopublications.
        """
        pass

    def create_nanopub_graphs(self):
        """
        Create the nanopublication(s) graph(s).
        """
        pass

    def getConjunctiveGraph(self):
        """
        Return the named graph.
        """
        return self.nanopub_graph

    def initializeFullGraph(self, identifier):
        """
        Initialize the graph and bind the namespaces.
        :param self: self object.
        :param identifier: (str) name of the graph.

        :return: self object, which is the updated graph.
        """
        # Get useful namespaces
        self.get_namespaces(identifier)

        graph_name = self.namespaces["npuri"][identifier]
        # Create the named graph
        self.nanopub_graph = ConjunctiveGraph(identifier=graph_name)

        return self

    def initializeGraph(self, identifier):
        """
        Initialize the graph and bind the namespaces.
        :param self: self object.
        :param identifier: (str) name of the graph.

        :return: self object, which is the updated graph.
        """
        # Get useful namespaces
        # self.get_namespaces()
        graph_name = self.namespaces["sub"][identifier]
        graph = Graph(store=self.nanopub_graph.store, identifier=graph_name)

        # Bind the imported namespaces (from rdflib.namespace) to a prefix for more readable output
        graph.bind("foaf", FOAF)
        graph.bind("xsd", XSD)
        graph.bind("rdfs", RDFS)
        graph.bind("rdf", RDF)
        graph.bind("dc", DC)
        graph.bind("dcterms", DCTERMS)

        # Bind the external ontologies
        for nid, uri in self.namespaces.items():
            graph.bind(nid, Namespace(uri))

        return graph

    def initializeNanopubGraphs(self):
        """
        Initialize all components of the extended_nanopub.
        :param self: self object.
        """
        # Initialize Head Graph
        self.head_graph = self.initializeGraph(f"head")

        # Link extended_nanopub's components to the head graph
        self.head_graph.add((
            self.nanopub_graph.identifier,
            RDF.type,
            NP.Nanopublication
        ))
        self.head_graph.add((
            self.nanopub_graph.identifier,
            NP.hasAssertion,
            self.namespaces["sub"]["assertion"],
        ))
        self.head_graph.add((
            self.nanopub_graph.identifier,
            NP.hasProvenance,
            self.namespaces["sub"]["provenance"],
        ))
        self.head_graph.add((
            self.nanopub_graph.identifier,
            NP.hasPublicationInfo,
            self.namespaces["sub"]["publicationInfo"],
        ))
        self.head_graph.add((
            self.nanopub_graph.identifier,
            NP.hasKnowledgeProv,
            self.namespaces["sub"]["knowledgeProv"],
        ))

        # Initialize all components
        self.assertion_graph = self.initializeGraph(f"assertion")
        self.pubinfo_graph = self.initializeGraph(f"pubinfo")
        self.provenance_graph = self.initializeGraph(f"provenance")
        self.knowledgeprov_graph = self.initializeGraph(f"knowledgeprov")

