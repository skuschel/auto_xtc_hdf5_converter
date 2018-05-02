#!/bin/bash
psanaXtcDataExtractor.py -e sxrx30116 -r 6 -c config/make_acq_eigen_basis.cfg -t
rm eigen_traces.h5 
mv sxrx30116run6.h5 eigen_traces.h5
psanaXtcDataExtractor.py -e sxrx30116 -r 6 -c config/acqiris_eigen_analysis.cfg  -t
python acqsvdtestsxrx30116run6.py &

