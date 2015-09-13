import urllib
import os, sys
import glob
import optparse


program = "download_bbc_samples.py"
version = "0.5"
usage = "Usage: %prog [OPTION]... [REST]"
description = "Demonstrates python code for GNU style arguments."

parser = optparse.OptionParser(usage=usage, version=version, description=description, prog=program)
parser.add_option("-d", "--directory", dest="directory", action="store",
                  help="download data to this directory" )
(options, args) = parser.parse_args()

if not options.directory:
    print "set -d <directory> to save data to"
    sys.exit(1)

DIRECTORY = options.directory

linkA = ['https://archive.org/download/orchestral_samples/BRASS.rar',
         'https://archive.org/download/orchestral_samples/STRINGS.rar',
         'https://archive.org/download/orchestral_samples/Woodwinds.rar',
         'https://archive.org/download/orchestral_samples/mandolin.rar'
         ]
for link in linkA:
    print "downloading: %s" % link
    urllib.urlretrieve(link, os.path.join(DIRECTORY, os.path.basename(link)))

os.chdir(DIRECTORY)
for file in glob.glob('*.rar'):
    cmd = 'unrar x %s' % file
    print "running: %s" % cmd
    os.system(cmd)

print "Done downloading and extracting to DIRECTORY: %s" % DIRECTORY
