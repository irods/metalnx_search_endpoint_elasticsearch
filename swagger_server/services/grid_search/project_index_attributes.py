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
        result.id = 'projects'
        result.info = 'Projects indexed from Epigenomics core'
        result.name = 'Epigenomics Projects'
        result.attributes = []

        result.attributes.append(IndexSearchAttributes(
            attrib_name='ASPNumber',
            attrib_example='2011-0016',
            attrib_type='String',
            attrib_path='ProjectApplication.ProjectInformation.ASPNumber',
            info='Animal Study Protocol approval number',
            shortcut_text='asp_number'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='Background',
            attrib_type='String',
            attrib_path='ProjectApplication.ScientificJustification.Background',
            info='Project background',
            shortcut_text='background'
        ))

        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='Consultation',
            attrib_type='String',
            attrib_path='ProjectApplication.ScientificJustification.Consultation',
            info='Project consultation',
            shortcut_text='consultation'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='CostEstimate',
            attrib_type='String',
            attrib_path='ProjectApplication.ScientificJustification.CostEstimate',
            info='Project cost estimate',
            shortcut_text='cost_estimate'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='DataAnalysisStrategy',
            attrib_type='String',
            attrib_path='ProjectApplication.ScientificJustification.DataAnalysisStrategy',
            info='Project data analysis strategy',
            shortcut_text='data_analysis_strategy'
        ))
        '''

        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='EstimatedDate',
            attrib_type='Date',
            attrib_path='ProjectApplication.ScientificJustification.EstimatedDate',
            info='Project estimated date',
            shortcut_text='estimated_date'
        ))
        '''

        result.attributes.append(IndexSearchAttributes(
            attrib_name='Hypothesis',
            attrib_type='String',
            attrib_path='ProjectApplication.ScientificJustification.Hypothesis',
            info='Project hypothesis',
            shortcut_text='project_hypothesis'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='IRBNumber',
            attrib_type='String',
            attrib_example='12-N-0095',
            attrib_path='ProjectApplication.ProjectInformation.IRBNumber',
            info='Institutional Review Board protocol number',
            shortcut_text='irb_number'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='Organism',
            attrib_type='String',
            attrib_example='Homo Sapiens',
            attrib_path='ProjectApplication.ProjectInformation.Organism',
            info='Organism used for research study',
            shortcut_text='organism'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='PIEmail',
            attrib_type='String',
            attrib_path='ProjectApplication.LabInformation.PIEmail',
            info='Principal investigator\'s email',
            shortcut_text='pi_email'
        ))

        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='PIID',
            attrib_type='String',
            attrib_path='ProjectApplication.LabInformation.PIID',
            info='Principal investigator\'s NIEHS ID',
            shortcut_text='pi_id'
        ))
        '''

        result.attributes.append(IndexSearchAttributes(
            attrib_name='PILab',
            attrib_type='String',
            attrib_example='DIR/EB',
            attrib_path='ProjectApplication.LabInformation.PILab',
            info='Principal investigator\'s research lab',
            shortcut_text='pi_lab'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='PIName',
            attrib_type='String',
            attrib_path='ProjectApplication.LabInformation.PIName',
            info='Principal investigator\'s NIEHS name',
            shortcut_text='pi_name'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectID',
            attrib_type='String',
            attrib_path='ProjectApplication.ProjectInformation.ProjectID',
            info='Abbreviated project title used for data delivery',
            shortcut_text='project_id'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectNumber',
            attrib_type='String',
            attrib_example='FY18-Pilot-Granny-Smith-001',
            attrib_path='ProjectApplication.ProjectInformation.ProjectNumber',
            info='Funding approval number issued by the Epigenomics core',
            shortcut_text='project_number'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectTitle',
            attrib_type='String',
            info='Project title',
            attrib_path='ProjectApplication.ProjectInformation.ProjectTitle',
            shortcut_text='project_title'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectType',
            attrib_type='String',
            attrib_example='Full, Pilot or Program',
            attrib_path='ProjectApplication.ProjectInformation.ProjectType',
            info='Project type',
            shortcut_text='project_type'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='Relevance',
            attrib_type='String',
            attrib_path='ProjectApplication.ScientificJustification.Relevance',
            info='Project relevance',
            shortcut_text='relevance'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='RequesterEmail',
            attrib_type='String',
            attrib_path='ProjectApplication.RequesterInformation.RequesterEmail',
            info='Project submitter\'s email',
            shortcut_text='requester_email'
        ))

        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='RequesterID',
            attrib_type='String',
            attrib_path='ProjectApplication.RequesterInformation.RequesterID',
            info='Project submitter\'s NIEHS id',
            shortcut_text='requester_id'
        ))
        '''

        result.attributes.append(IndexSearchAttributes(
            attrib_name='RequesterName',
            attrib_type='String',
            attrib_path='ProjectApplication.RequesterInformation.RequesterName',
            info='Project submitter\'s name',
            shortcut_text='requester_name'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='SequencingFacility',
            attrib_type='String',
            attrib_path='ProjectApplication.ProjectInformation.SequencingFacility',
            info='Sequencing facility',
            shortcut_text='sequencing_facility'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='url',
            attrib_type='String',
            attrib_path='ProjectApplication.ProjectInformation.dc_url',
            info='Data commons location path',
            shortcut_text='url'
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='Validation',
            attrib_type='String',
            attrib_path='ProjectApplication.ScientificJustification.Validation',
            info='Project validation',
            shortcut_text='validation'
        ))

        return result
