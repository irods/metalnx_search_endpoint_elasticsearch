from swagger_server.models import Indexes


class NotFoundError(Exception):
        pass


class EpigenomicsSearchAdapter:
    """Supports Epigenomics core Elastic search functions provided to the standard API"""

    def __init__(self):
        """
        Parameters

        """

        pass

    @staticmethod
    def describe_index():
        """
        Describe the capabilities of this particular index server
        :return: index
        """

        index_search = Indexes()
        index_search.id = "niehs-epigenomics"
        index_search.name = "Epigenomics ElasticSearch Indexes"
        index_search.info = "NIEHS Data Commons search for Epigenomics data via project and sample information"
        indexes = []
        index_entry = Indexes()
        index_entry.id = "projects"
        index_entry.name = "Epigenomics Projects"
        index_entry.maintainer = "ODS"
        index_entry.contact_email = "mike.conway@nih.gov"
        index_entry.info = "Search of project request information, hypothesis, purpose, etc. " \
                           "as entered during the project approval phase"
        indexes.append(index_entry)
        index_entry = Indexes()
        index_entry.id = "samples"
        index_entry.name = "Epigenomics Samples and Runs"
        index_entry.info = "Search of sequencing runs and samples"
        index_entry.maintainer = "ODS"
        index_entry.contact_email = "mike.conway@nih.gov"
        indexes.append(index_entry)

        index_search.indexes = indexes

        return index_search
