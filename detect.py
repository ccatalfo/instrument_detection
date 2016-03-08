import sys
import numpy as np
import data
import optparse
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


program = "detect.py"
version = "0.1"
usage = "Usage: %prog [OPTION]... [REST]"
description = "Instrument detection using scikit-learn"

parser = optparse.OptionParser(usage=usage, version=version, description=description, prog=program)
parser.add_option("-d", "--directory", dest="directory", action="store",
                  help="download data to this directory" )
(options, args) = parser.parse_args()

if not options.directory:
    print "set -d <directory> to save data to"
    sys.exit(1)
logger.info('loading dataset from directory: %s' % options.directory)

DIRECTORY = options.directory
dataset  = data.load_dataset(DIRECTORY)
target_names = [item['target'] for item in dataset]
unique_tarets = np.unique(target_names)
logger.info('%d targets found: %s' % (len(unique_tarets), unique_tarets))




