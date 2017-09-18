# -*- coding: utf-8 -*-
import os
import pathlib

_FILE_PATH = pathlib.Path(os.path.realpath(__file__))

DOMAIN = os.environ['TRAVIS_REPO_SLUG'].split('/')[1]
WEBSITE_DIR = _FILE_PATH.parent.parent.parent / 'website'
TEMP_DIR = pathlib.Path('/dev/shm')
DIST_NAME = DOMAIN
DIST_DIR = TEMP_DIR / DIST_NAME
DIST_ARCHIVE = DIST_DIR.with_suffix('.tar.gz')

S3_PROD_BUCKET = DOMAIN
S3_QA_BUCKET = f'qa.{DOMAIN}'
S3_REGION = 'eu-west-1'
S3_STORAGE_CLASS = 'STANDARD'
