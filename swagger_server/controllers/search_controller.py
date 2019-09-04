import connexion
import six
import logging

from swagger_server.models.search_data import SearchData  # noqa: E501
from swagger_server.services.grid_search.generic_search import GenericSearch
from werkzeug.exceptions import BadRequest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)


def generic_search(index_name, search_query):  # noqa: E501
    """Generic search on one or all available indexes

    Returns result hits with associated fields and values # noqa: E501

    :param index_name:
    :type index_name: str
    :param search_query:
    :type search_query: str

    :rtype: SearchData
    """

    # TODO: this is a bit weird but is supposed to represent a translation from
    # generic index name and ES index name. For now they are the same

    if index_name == "projects":
        my_index_name = "projects"
    else:
        my_index_name = "samples"

    logger.debug('search_controller: generic_search()')
    if my_index_name is not None and search_query is not None:
        logger.debug('args: \n index_name: %s \n search_query: %s' % (my_index_name, search_query))
        gs = GenericSearch()
        search_dsl = gs.generate_generic_dsl(search_query)
        logger.debug("search_dsl:: %s" % search_dsl)

        if len(search_dsl) > 0:
            result = gs.generic_search(my_index_name, search_dsl)
            return result
        else:
            raise BadRequest("Bad Request: Invalid search query")
