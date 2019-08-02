from swagger_server.models import Index


class EpigenomicsSearchAdapter:
    """Supports Epigenomics core Elastic search functions provided to the standard API"""

    def __init__(self):
        """
        Parameters

        """

        pass

    def describe_index(self):
        """
        Describe the capabilities of this particular index server
        :return: index
        """

        index_search = Index()
        index_search.id ="niehs-epigenomics"
        index_search.name = "Epigenomics ElasticSearch Indexes"
        index_search.info ="NIEHS Data Commons search for Epigenomics data via project and sample information"
        return index_search
