#!/bin/bash
psplot -s psanaphi104 -p 12303 eigen_system_Acq02 &
../../psanaXtcDataExtractor.py -e xpptut15 -r 440 -c config/make_acq_eigen_basis.cfg
rm eigen_traces.h5 
mv hdf5/xpptut15run440.h5 hdf5/xpptut15run440_eigen_basis.h5
../../psanaXtcDataExtractor.py -e xpptut15 -r 440 -c config/acqiris_eigen_analysis.cfg  -t
python acqsvdtestxpptut15run440.py &
python acqsvdtestxpptut15run440.py &
python acqsvdtestxpptut15run440.py &

