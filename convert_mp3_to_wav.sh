#!/bin/bash
# pass in top level directory
# ./convert_mp3_to_wav.sh /bbc_data 
find $1/ -name "*.mp3" -exec bash -c 'mpg123 -w ${0/mp3/wav} $0' {} \; 
