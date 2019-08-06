import connexion
import six
from flask_restful import abort

from grid_search.epigenomics_search_adapter import EpigenomicsSearchAdapter, NotFoundError
from swagger_server.models.indexes import Indexes  # noqa: E501
from swagger_server.models.search_attributes import SearchAttributes  # noqa: E501
from swagger_server import util


def get_indexes():  # noqa: E501
    """Find index types supported by this api

    Returns a summary list of the search indexes available at this endpoint # noqa: E501


    :rtype: Indexes
    """

    adapter = EpigenomicsSearchAdapter()
    return adapter.describe_index()


def get_index_search_attributes(index_name):  # noqa: E501
    """Find search attribute terms for a specific index

    Returns a list of search attribute terms available for specified index # noqa: E501

    :param index_name:
    :type index_name: str

    :rtype: SearchAttributes
    """
    adapter = EpigenomicsSearchAdapter()

    try:
        return adapter.search_attributes(index_name)
    except NotFoundError:
        abort(404)
