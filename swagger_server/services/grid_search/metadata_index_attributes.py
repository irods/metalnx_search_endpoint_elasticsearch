from swagger_server.models import IndexSearchAttributes, SearchAttributes


class MetadataIndexAttributes:
    # ToDo: Currently attributes are hardcoded need to see if information can be directly retrieved from ES
    # ToDo: Add a field to contain example of each search attribute
    @staticmethod
    def search_attributes():
        """
        Parse index attribute and an particular index
        :return: searchAttributes
        """
        result = SearchAttributes()
        result.id = 'metadata'
        result.info = 'AVUs indexed from iRODS catalog'
        result.name = 'metadata'
        result.attributes = [
            IndexSearchAttributes(
                attrib_name='zoneName',
                attrib_path='zoneName',
                attrib_type='String',
                attrib_example='tempZone',
                info='iRODS zone name',
                shortcut_text='zoneName'
            ),
            IndexSearchAttributes(
                attrib_name='fileName',
                attrib_path='fileName',
                attrib_type='String',
                attrib_example='foo.txt',
                info='Name of the file',
                shortcut_text='fileName'
            ),
            IndexSearchAttributes(
                attrib_name='isFile',
                attrib_path='isFile',
                attrib_type='Boolean',
                attrib_example='True',
                info='Is it file',
                shortcut_text='isFile'
            ),
            IndexSearchAttributes(
                attrib_name='dataSize',
                attrib_path='dataSize',
                attrib_type='Numeric',
                attrib_example='123',
                info='Size a file or folder in (kb!)',
                shortcut_text='dataSize'
            ),
            IndexSearchAttributes(
                attrib_name='mimeType',
                attrib_path='mimeType',
                attrib_type='String',
                attrib_example='image/jpeg',
                info='Mime type of file',
                shortcut_text='mimeType'
            ),
            IndexSearchAttributes(
                attrib_name='lastModifiedDate',
                attrib_path='lastModifiedDate',
                attrib_type='Date',
                attrib_example='add date format example',
                info='Last modification date saved in index',
                shortcut_text='lastModifiedDate'
            ),
            IndexSearchAttributes(
                attrib_name='attribute',
                attrib_path='metadataEntries.attribute',
                attrib_type='String',
                attrib_example='attrib1',
                info='Attribute part of AVU triple',
                shortcut_text='attribute'
            ),
            IndexSearchAttributes(
                attrib_name='value',
                attrib_path='metadataEntries.value',
                attrib_type='String',
                attrib_example='value1',
                info='Value part of AVU triple',
                shortcut_text='value'
            ),
            IndexSearchAttributes(
                attrib_name='unit',
                attrib_path='metadataEntries.unit',
                attrib_type='String',
                attrib_example='unit1',
                info='Unit part of AVU triple',
                shortcut_text='unit'
            )

        ]
        return result
