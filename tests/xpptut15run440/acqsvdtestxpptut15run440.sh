#!/bin/bash
../../psanaXtcDataExtractor.py -e xpptut15 -r 440 -c config/make_acq_eigen_basis.cfg -t
rm eigen_traces.h5 
mv hdf5/xpptut15run440.h5 hdf5/xpptut15run440_eigen_basis.h5
../../psanaXtcDataExtractor.py -e xpptut15 -r 440 -c config/acqiris_eigen_analysis.cfg  -t
python acqsvdtestxpptut15run440.py &
python acqsvdtestxpptut15run440.py &
python acqsvdtestxpptut15run440.py &

