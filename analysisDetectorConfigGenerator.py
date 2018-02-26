#!/reg/g/psdm/sw/conda/inst/miniconda2-prod-rhel7/envs/ana-1.3.9/bin/python
#from pylab import *
import sys
import os
sys.path.append(os.curdir) 
import argparse
import psana
import IPython

#--------------------------------------------------------------------------
# File and Version Information:
#  $Id: README  2017-08-06 18:54:12Z sioan@SLAC.STANFORD.EDU $
#
# Description:
#  README file for data analysis
#------------------------------------------------------------------------

#Package author: Sioan Zohar

#Brief description:
#==================
#This generates the config file used for the psanaXtcDataExtractor.py
#
#==================
#to do: figure out why touching __init__.py doesn't create file.  Solved.  White space before __init__.py
def write_config_file(configFileName,config_type):

	f = open('./config/'+configFileName,'w')
	print("writing libraries")

	f.write('##########################\n')
	f.write('#######DAQ DEVICES########\n')
	f.write('##########################\n')

	for thisDetectorName in psana.DetNames():
		is_acqiris = (True in ['Acqiris' in i for i in  thisDetectorName])
		#IPython.embed()

		f.write('#')
		det_desc = []
		for i in thisDetectorName:
			f.write(str(i)+',')
			det_desc.append(i)
			
			#f.write(' detectorFinish')

		if(is_acqiris):
			if("make_acq_basis"==config_type):
					f.write(det_desc[-2]+',None,make_acq_svd_basis,\n')

			elif("use_acq_basis"==config_type):
					f.write(det_desc[-2]+',use_acq_svd_basis,None,\n')
			else:
				f.write('\n')
		else:
			f.write('\n')
	f.write('##########################\n')
	f.write('#######EPICS PVs##########\n')
	f.write('##########################\n')

	for thisDetectorName in psana.DetNames('epics'):
		f.write('#')
		for i in thisDetectorName:
			f.write(str(i)+', ')
		#f.write(' epicsPvFinish')
		f.write('\n')
	f.close()


def main(exp, run, configFileName):
	
	experimentNameAndRun = "exp=%s:run=%d"%(exp, run)
	print("current working directory"+str(os.curdir))	
	os.system('mkdir config')
	print("creating libraries")
	os.system('touch config/__init__.py')

	print("initializing")
	myDataSource = psana.MPIDataSource(experimentNameAndRun)

	write_config_file(configFileName,"default")
	write_config_file("make_acq_eigen_basis.cfg","make_acq_basis")
	write_config_file("acqiris_eigen_analysis.cfg","use_acq_basis")
	
	os.system("cp /reg/g/psdm/sw/hutch/sxd/auto_xtc_hdf5_converter/config/analysisFunctions.py ./config/")
	

if __name__ == '__main__':
	myParser = argparse.ArgumentParser(description='Generating a config file for analysis')
	#myGroup = myParser.add_mutually_exclusive_group()
	
	myParser.add_argument('-e','--exp', help='the experiment name')
	myParser.add_argument('-r','--run',type=int,help='the run number to use when running offline')
	myParser.add_argument('-c','--configFile',help='the config file to write to',default="analysis.cfg")

	myArguments = myParser.parse_args()

	main(myArguments.exp,myArguments.run,myArguments.configFile)
