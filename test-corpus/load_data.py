#!/usr/bin/env python3

# title           : load_data.py
# description     :Uses Elastic Search api to:
#                      - initiate/create index if mapping document is provided
#                      - load serialized JSON documents to corresponding index
# author          :Deep Patel
# usage           :python3 load_data.py
#                       -b elasticSearch_baseURL \
#                       -m path_to_folder_containing_index_mapping
#                       -p path_to_folder_containing_poroject_jsons \
#                       -s path_to_folder_containing_sample_jsons \
#
# python_version  :3.7.0
# =============================================================================


import json
import logging
import sys
import os
import fnmatch

from swagger_server.api import APIUtils
from optparse import OptionParser

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s:%(funcName)s:%(lineno)d: %(message)s"
)

logger = logging.getLogger(__name__)

# Indexes to be used in ES
PROJECT = 'projects'
SAMPLE = 'samples'


class LoadData:
    def __init__(self):
        self.mapping_folder_path = ''
        self.project_folder_path = ''
        self.sample_folder_path = ''
        self.base_url = ''
        self.api = APIUtils()

    def setup(self, base_url, mapping_folder_path, project_folder_path, sample_folder_path):
        self.base_url = base_url
        self.mapping_folder_path = mapping_folder_path
        self.project_folder_path = project_folder_path
        self.sample_folder_path = sample_folder_path
        self.api.setup(self.base_url)

    def create_indexes(self):
        """
        Scans mapping folder path for specific mapping file_names if present create's corresponding index
        project: project_mapping.json
        sample: samples_mapping.json
        """
        for file in os.listdir(self.mapping_folder_path):
            if fnmatch.fnmatch(file, 'project_mapping.json'):
                logger.info("Project mapping file found!")
                file_path = os.path.join(self.mapping_folder_path, file)
                with open(file_path) as data:
                    json_data = json.loads(data.read())
                    self.api.create_index_with_mapping(PROJECT, json_data)
            elif fnmatch.fnmatch(file, 'sample_mapping.json'):
                logger.info("Sample mapping file found!")
                file_path = os.path.join(self.mapping_folder_path, file)
                with open(file_path) as data:
                    json_data = json.loads(data.read())
                    self.api.create_index_with_mapping(PROJECT, json_data)

    def load_index_docs(self):
        """
        Scan for JSON docs and add to corresponding index
        """

        # loading project docs
        proj_res = {'counter': 0, 'project_id_list': []}
        for file in os.listdir(self.project_folder_path):
            if fnmatch.fnmatch(file, '[!.]*.json'):
                file_path = os.path.join(self.project_folder_path, file)
                logger.info("Project JSON found: %s" % file_path)
                with open(file_path) as data:
                    project_json_data = json.loads(data.read())
                    project_id = project_json_data["ProjectID"]

                    # Add project doc to ES index "projects"
                    logger.debug('\n\n_____________________________________________')
                    logger.debug('Adding project doc to ES index projects')
                    logger.debug('Index name: ' + PROJECT)
                    logger.debug('project_id: ' + project_id)
                    logger.debug('json_data: ' + str(project_json_data))

                    result = self.api.add_index_doc(PROJECT, project_id, project_json_data)
                    if result.status_code == 201:
                        proj_res['counter'] += 1
                        proj_res['project_id_list'].append(project_id)
        logger.info("\nProject loading completed.\n\nSummary for project index:")
        logger.info("Total projects added :: %d " % proj_res['counter'])
        logger.info("List of project_ids :: %s" % str(proj_res['project_id_list']))

        # loading sample docs
        sample_res = {'counter': 0, 'sample_id_list': []}
        for file in os.listdir(self.sample_folder_path):
            if fnmatch.fnmatch(file, '[!.]*.json'):
                file_path = os.path.join(self.sample_folder_path, file)
                logger.info("Sample JSON found: %s" % file_path)
                with open(file_path) as data:
                    sample_json_data = json.loads(data.read())
                    sample_id = sample_json_data["SampleName_unique"]

                    # Add sample doc to RS index "samples"
                    logger.debug('\n\n_____________________________________________')
                    logger.debug('Adding sample doc to ES index samples')
                    logger.debug('Index name: ' + SAMPLE)
                    logger.debug('sample_id: ' + sample_id)
                    logger.debug('json_data: ' + str(sample_json_data))

                    result = self.api.add_index_doc(SAMPLE, sample_id, sample_json_data)
                    if result.status_code == 201:
                        sample_res['counter'] += 1
                        sample_res['sample_id_list'].append(sample_id)
        logger.info("\nSample loading completed.\n\nSummary for sample index:")
        logger.info("Total samples added :: %d " % sample_res['counter'])
        logger.info("List of sample_ids :: %s" % str(sample_res['sample_id_list']))


def setup_arguments():
    parser = OptionParser()
    parser.add_option('-b', "--baseURL", action='store', dest='base_url')
    parser.add_option('-p', "--projectFolder", action='store', dest='project_folder')
    parser.add_option('-s', "--sampleFolder", action='store', dest='sample_folder')
    parser.add_option('-m', "--mappingFolder", action='store', dest='mapping_folder')
    return parser.parse_args()[0]


def main():
    logger.info('Main function execution started.')
    global args
    args = setup_arguments()

    if len(sys.argv) > 1:
        base_url = args.base_url.rstrip('/')
        project_folder = args.project_folder.rstrip('/')
        sample_folder = args.sample_folder.rstrip('/')
        mapping_folder = args.mapping_folder.rstrip('/')

        logger.info("ES base url :: %s" % base_url)
        logger.info("index mapping folder:: %s" % mapping_folder)
        logger.info("Project folder path :: %s" % project_folder)
        logger.info("Sample folder path :: %s" % sample_folder)

        if not os.path.exists(project_folder) or not os.path.exists(sample_folder) or \
                not os.path.exists(mapping_folder):
            logger.error("ERROR: Folder/s does not exists. System will exit now...")
            sys.exit()

        load_es = LoadData()
        logger.info("Initiating LoadData class object.")
        load_es.setup(base_url, mapping_folder, project_folder, sample_folder)

        logger.info("Scanning index mapping folder and creating indexes.")
        load_es.create_indexes()

        logger.info("Loading JSON docs to indexes: projects and samples ...")
        load_es.load_index_docs()


if __name__ == "__main__":
    main()
