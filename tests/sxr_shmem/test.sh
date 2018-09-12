#!/bin/bash
echo `hostname`
export PYTHONPATH=""
export LD_LIBRARY_PATH=""
source /reg/g/psdm/etc/psconda.sh

export PATH="/reg/g/psdm/sw/conda/inst/miniconda2-prod-rhel7/envs/ana-1.3.52/bin:/reg/g/psdm/sw/conda/manage/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin"
../../psanaXtcDataExtractor.py -e sxrlu2017 -r 30 -shmem
