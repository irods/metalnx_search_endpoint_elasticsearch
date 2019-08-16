from swagger_server.models import IndexSearchAttributes, SearchAttributes


class SampleIndexAttributes:
    # ToDo: Currently attributes are hardcoded need to see if information can be directly retrieved from ES
    # ToDo: Add a field to contain example of each search attribute
    @staticmethod
    def search_attributes():
        """
        Parse index attribute and an particular index
        :return: searchAttributes
        """
        result = SearchAttributes()
        result.id = 'EpigenomicsSamplesandRuns'
        result.info = 'Samples and runs indexed from Epigenomics core'
        result.name = 'Epigenomics Samples and Runs'
        result.attributes = []

        attribute_entry = IndexSearchAttributes(
            attrib_name='Run Id',
            attrib_type='String',
            info='Run Id assigned in the sample sheet',
            shortcut_text='runid'
        )
        result.attributes.append(attribute_entry)
        return result
