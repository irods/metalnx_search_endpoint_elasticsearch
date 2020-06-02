from swagger_server.models import Indexes


class NotFoundError(Exception):
        pass


class SearchAdapter:
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
        index_search.id = "epigenomics"
        index_search.name = "Metadata ElasticSearch Indexes"
        index_search.info = "Epigenomics core data search using metadata index"

        indexes = [Indexes(
            id="metadata",
            es_id="metadata",
            name="Metadata Search",
            info="AVUs indexed from iRODS catalog",
            maintainer="John Doe",
            contact_email="john.doe@example.com"
        )]
        index_search.indexes = indexes

        return index_search
