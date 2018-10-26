#!/bin/bash
../../psanaXtcDataExtractor.py -e xpptut15 -r 350
rm eigen_traces.h5
python show_test_results.py 
