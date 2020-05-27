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
        result.id = 'samples'
        result.info = 'Samples and runs indexed from Epigenomics core'
        result.name = 'Epigenomics Samples and Runs'
        result.attributes = []

        result.attributes.append(IndexSearchAttributes(
            attrib_name='AnalystEmail',
            attrib_path='SampleEntries.AnalystEmail',
            attrib_type='String',
            attrib_example='brian.papas@nih.gov',
            info='Email ID of the analyst',
            shortcut_text='analyst_email'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='AnalystName',
            attrib_path='SampleEntries.AnalystName',
            attrib_type='String',
            attrib_example='Brian Papas',
            info='Name of the analyst',
            shortcut_text='analyst_name'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ASPNumber',
            attrib_path='ASPNumber',
            attrib_type='String',
            attrib_example='2011-0016',
            info='Animal Study Protocol approval number',
            shortcut_text='asp_number'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='Branch',
            attrib_path='Branch',
            attrib_type='String',
            attrib_example='DIR/STL',
            info='Branch name, affiliated with project PI',
            shortcut_text='branch'
        ))
        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='CaptureMethod',
            attrib_path='CaptureMethod',
            attrib_type='String',
            attrib_example='',
            info='Single cell capture method, only for single cell experiments',
            shortcut_text='capture_method'
        ))
        '''
        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='CellTissueType',
            attrib_type='String',
            attrib_example='Mouse Peritoneal Macrophages',
            info='Cell or Tissue type',
            shortcut_text='cell_tissue_type'
        ))
        '''

        result.attributes.append(IndexSearchAttributes(
            attrib_name='Date',
            attrib_path='Date',
            attrib_type='String',
            attrib_example='',
            info='Date of sample submission form',
            shortcut_text=''
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='GenomeRef',
            attrib_path='SampleEntries.GenomeRef',
            attrib_type='String',
            attrib_example='mm10',
            info='',
            shortcut_text='genome_ref'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='Index1',
            attrib_path='SampleEntries.Index1',
            attrib_type='String',
            attrib_example='AGTTCC',
            info='',
            shortcut_text='index_1'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='Index2',
            attrib_path='SampleEntries.Index2',
            attrib_type='String',
            attrib_example='AGTTCC',
            info='',
            shortcut_text='index_2'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='IRBNumber',
            attrib_path='IRBNumber',
            attrib_type='String',
            attrib_example='12-N-0095',
            info='Institutional Review Board protocol number',
            shortcut_text='irb_number'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='LibrariesPreparedBy',
            attrib_path='LibrariesPreparedBy',
            attrib_type='String',
            attrib_example='Investigator',
            info='Was the library prepared by Investigator or Epigenomics Core',
            shortcut_text='libraries_prepared_by'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='LibraryPurchasedBy',
            attrib_path='LibraryPurchasedBy',
            attrib_type='String',
            attrib_example='Investigator',
            info='Was NGS library preparation kit purchased by Investigator or Epigenomics Core',
            shortcut_text='library_purchased_by'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='PIEmail',
            attrib_path='PIEmail',
            attrib_type='String',
            attrib_example='',
            info='Principal investigator email',
            shortcut_text=''
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='PIName',
            attrib_path='PiName',
            attrib_type='String',
            attrib_example='Bell, Douglas A.',
            info='Principal investigator name',
            shortcut_text=''
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='PreparationKit',
            attrib_path='SampleEntries.PreparationKit',
            attrib_type='String',
            attrib_example='Nextera without indexing',
            info='NGS library preparation kit',
            shortcut_text='preparation_kit'
        ))


        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectID',
            attrib_path='ProjectID',
            attrib_type='String',
            attrib_example='',
            info='Abbreviated project title',
            shortcut_text=''
        ))

        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectNumber',
            attrib_path='ProjectNumber',
            attrib_type='String',
            attrib_example='FY18-Program-Bell-001',
            info='Funding approval number issued by the Epigenomics core',
            shortcut_text='project_number'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ProjectTitle',
            attrib_path='ProjectTitle',
            attrib_type='String',
            attrib_example='226M_Trial_CombIndex',
            info='Project title',
            shortcut_text='project_title'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='QuantificationMethod',
            attrib_path='SampleEntries.QuantificationMethod',
            attrib_type='String',
            attrib_example='Qubit',
            info='Nucleic acid quantification method',
            shortcut_text='quantification_method'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ReadCounts',
            attrib_path='SampleEntries.ReadCounts',
            attrib_type='Numeric',
            attrib_example='66288',
            info='Total read count for all the samples in this submission',
            shortcut_text='read_counts'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ReadLength',
            attrib_path='SampleEntries.ReadLength',
            attrib_type='String',
            attrib_example='75 nt',
            info='Requested read length for a specific sample',
            shortcut_text='read_length'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='ReadsNeeded',
            attrib_path='SampleEntries.ReadsNeeded',
            attrib_type='Numeric',
            attrib_example='40',
            info='Requested number of reads per sample, x10^6',
            shortcut_text='reads_needed'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='RequesterEmail',
            attrib_path='RequesterEmail',
            attrib_type='String',
            attrib_example='suzanne.martos@nih.gov',
            info='Sample submitter\'s email',
            shortcut_text='requester_email'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='RequesterName',
            attrib_path='RequesterName',
            attrib_type='String',
            attrib_example='Martos, Suzanne N.',
            info='Sample submitter\'s name',
            shortcut_text='requester_name'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='RunId',
            attrib_path='RunId',
            attrib_type='String',
            attrib_example='MES1328',
            info='Instrument run ID',
            shortcut_text='runid'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SampleConcentration',
            attrib_path='SampleEntries.SampleConcentration',
            attrib_type='Numeric',
            attrib_example='43',
            info='Sample Concentration',
            shortcut_text='sample_concentration'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SampleName',
            attrib_path='SampleEntries.SampleName',
            attrib_type='String',
            attrib_example='4H5-PRCseq-Ovi25',
            info='Sample name',
            shortcut_text='sample_name'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SampleNumber',
            attrib_path='SampleEntries.SampleNumber',
            attrib_type='Numeric',
            attrib_example='2',
            info='Number of samples in submission',
            shortcut_text='sample_number'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SampleSource',
            attrib_path='SampleEntries.SampleSource',
            attrib_type='String',
            attrib_example='cell line, tissue, saliva',
            info='Sample source',
            shortcut_text='sample_source'
        ))

        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SampleType',
            attrib_type='String',
            attrib_example='dna',
            info='Sample specimen handed to Epigenomics Core',
            shortcut_text='sample_type'
        ))
        '''
        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SampleWellLocation',
            attrib_type='String',
            attrib_example='A:12',
            info='Location of sample on 96-plate',
            shortcut_text='sample_well_location'
        ))
        '''

        result.attributes.append(IndexSearchAttributes(
            attrib_name='SeqApplication',
            attrib_path='SampleEntries.SeqApplication',
            attrib_type='String',
            attrib_example='Single-Cell RNAseq, ATAC-seq',
            info='Sequencing application',
            shortcut_text='seq_application'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SeqFormat',
            attrib_path='SampleEntries.SeqFormat',
            attrib_type='String',
            attrib_example='single, paired',
            info='Sequencing format',
            shortcut_text='seq_format'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SeqSystem',
            attrib_path='SampleEntries.SeqSystem',
            attrib_type='String',
            attrib_example='MiSeq',
            info='Sequencing format',
            shortcut_text='seq_system'
        ))
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SequencingFacility',
            attrib_path='SequencingFacility',
            attrib_type='string',
            attrib_example='NIEHS Core',
            info='Sequencing facility',
            shortcut_text='sequencing_facility'
        ))

        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SingleCell',
            attrib_type='Boolean',
            attrib_example='false',
            info='Is it a single cell experiment',
            shortcut_text=''
        ))
        '''

        result.attributes.append(IndexSearchAttributes(
            attrib_name='Species',
            attrib_path='SampleEntries.Species',
            attrib_type='String',
            attrib_example='Homo sapiens',
            info='Species',
            shortcut_text='species'
        ))

        '''
        result.attributes.append(IndexSearchAttributes(
            attrib_name='SampleSheetName',
            attrib_type='String',
            attrib_example='',
            info='Sample submission file name',
            shortcut_text='sample_sheet_name'
        ))
        '''
        return result
