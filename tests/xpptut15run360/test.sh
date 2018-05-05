#!/bin/bash
../../psanaXtcDataExtractor.py -e xpptut15 -r 360 -f 5000
rm eigen_traces.h5
python show_test_results.py
