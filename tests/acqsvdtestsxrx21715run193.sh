#!/bin/bash
psanaXtcDataExtractor.py -e sxrx21715 -r 193 -c config/make_acq_eigen_basis.cfg -t
rm eigen_traces.h5 
mv sxrx21715run193.h5 eigen_traces.h5
psanaXtcDataExtractor.py -e sxrx21715 -r 193 -c config/acqiris_eigen_analysis.cfg  -t
python acqsvdtestsxrx21715run193.py &

