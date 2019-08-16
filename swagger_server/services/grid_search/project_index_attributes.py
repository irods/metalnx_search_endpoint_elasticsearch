from swagger_server.models import IndexSearchAttributes, SearchAttributes


class ProjectIndexAttributes:

    # ToDo: Currently attributes are hardcoded need to see if information can be directly retrieved from ES
    # ToDo: Add a field to contain example of each search attribute
    @staticmethod
    def search_attributes():
        """
        Parse index attribute and an particular index
        :return: searchAttributes
        """
        result = SearchAttributes()
        result.id = 'EpigenomicsProjects'
        result.info = 'Projects indexed from Epigenomics core'
        result.name = 'Epigenomics Projects'
        result.attributes = []

        result.attributes.append(IndexSearchAttributes(
            attrib_name='url',
            attrib_type='String',
            info='iRODS collection location path',
            shortcut_text='url'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='PIEmail',
            attrib_type='String',
            info='Principal investigator\'s email address',
            shortcut_text='pi_email'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='PIID',
            attrib_type='String',
            info='Principal investigator\'s NIEHS ID',
            shortcut_text='pi_id'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='PILab',
            attrib_type='String',
            info='Principal investigator\'s research lab',
            shortcut_text='pi_lab'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='ASPNumber',
            attrib_type='String',
            info='Animal Study Protocol approval number',
            shortcut_text='asp_number'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='IRBNumber',
            attrib_type='String',
            info='Institutional Review Board protocol number',
            shortcut_text='irb_number'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='Organism',
            attrib_type='String',
            info='Organism used for research study',
            shortcut_text='organism'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectID',
            attrib_type='String',
            info='Abbreviated project title used for data delivery',
            shortcut_text='project_id'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectNumber',
            attrib_type='String',
            info='Funding approval number issued by the Epigenomics core',
            shortcut_text='project_number'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectTitle',
            attrib_type='String',
            info='Project title',
            shortcut_text='project_title'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectType',
            attrib_type='String',
            info='Project type',
            shortcut_text='project_type'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SequencingFacility',
            attrib_type='String',
            info='Sequencing facility',
            shortcut_text='sequencing_facility'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='RequesterEmail',
            attrib_type='String',
            info='Project submitter\'s email',
            shortcut_text='requester_email'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='RequesterID',
            attrib_type='String',
            info='Project submitter\'s NIEHS id',
            shortcut_text='requester_id'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='RequesterName',
            attrib_type='String',
            info='Project submitter\'s name',
            shortcut_text='requester_name'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='Background',
            attrib_type='String',
            info='Project background',
            shortcut_text='background'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='Consultation',
            attrib_type='String',
            info='Project consultation',
            shortcut_text='consultation'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='CostEstimate',
            attrib_type='String',
            info='Project cost estimate',
            shortcut_text='cost_estimate'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='DataAnalysisStrategy',
            attrib_type='String',
            info='Project data analysis strategy',
            shortcut_text='data_analysis_strategy'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='EstimatedDate',
            attrib_type='Date',
            info='Project estimated date',
            shortcut_text='estimated_date'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='Hypothesis',
            attrib_type='String',
            info='Project hypothesis',
            shortcut_text='project_hypothesis'
        ))
        return result
