import connexion
import six

from swagger_server.models.indexes import Indexes  # noqa: E501
from swagger_server import util


def get_indexes():  # noqa: E501
    """Find index types supported by this api

    Returns a summary list of the search indexes available at this endpoint # noqa: E501


    :rtype: Indexes
    """
    return 'do some magic!'
