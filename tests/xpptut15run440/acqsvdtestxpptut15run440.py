#!/reg/g/psdm/sw/conda/inst/miniconda2-prod-rhel7/envs/ana-1.3.9/bin/python -i
from pylab import *
import h5py
import argparse
import sys
import IPython
import psana

def hdf5_to_dict(myhdf5Object):
	replacementDictionary = {}
	for i in myhdf5Object:
		print(str(myhdf5Object[i]))
		if ('dataset' in str(myhdf5Object[i])):
			print("dataset is in"+str(myhdf5Object[i]))
			if ('Summarized' not in str(myhdf5Object[i])):
				replacementDictionary[i] = nan_to_num(myhdf5Object[i])
			else:
				x=1	
		else:
			replacementDictionary[i] = {}
			print("dataset is not in"+str(myhdf5Object[i]))
			print(i)
			replacementDictionary[i] = hdf5_to_dict(myhdf5Object[i])

	return replacementDictionary

def main(fileName):
	global my_dict
	my_hdf5_object = h5py.File("hdf5/xpptut15run440.h5",'r')
	#convert hdf5 to dict
	my_list = []
	def func(name, obj):
		my_list.append(name)

	my_hdf5_object.visititems(func)
	my_dict = {}
	
	for i in my_list:
		try:
			my_dict[i] = array(my_hdf5_object[i])
		except:
			#IPython.embed()
			pass

	my_hdf5_object.close()

	#%matplotlib
	acqiris_alias="Acq02"
	eigen_basis_file = "hdf5/xpptut15run440_eigen_basis.h5"
	experiment_name = "xpptut15"
	run_number = "440"
	channel_number=3
	event_number = int(200 * rand())
	print("event number number for testing: "+str(event_number))
	####################
	#####################

	my_eigen_basis = h5py.File(eigen_basis_file)
	eig_bas = array(my_eigen_basis['summary/nonMeaningfulCoreNumber0/'+acqiris_alias+'/ch'+str(channel_number)+'/norm_eigen_wave_forms'])
	import psana
	my_data_source = psana.MPIDataSource("exp="+experiment_name+":run="+run_number+":smd")
	acq_det_obj = psana.Detector(acqiris_alias)
	my_enum_events = enumerate(my_data_source.events())
	for evt_num,this_event in my_enum_events:
		if evt_num>event_number:
		    break
	my_index=argmax((this_event.get(psana.EventId).fiducials() == my_dict['fiducials']).astype(int))
	#plot(acq_det_obj(this_event)[0][channel_number]-mean(acq_det_obj(this_event)[0][channel_number][:300]))

	plot(acq_det_obj(this_event)[0][channel_number]-mean(acq_det_obj(this_event)[0][channel_number][:300]))
	plot(dot(my_dict[acqiris_alias+'/ch'+str(channel_number)+'/weightings'][evt_num], eig_bas),'r.')
	ylim(-0.06,0.0)
	xlim(1100,1400)
	show()

if __name__ == '__main__':

	#myParser = argparse.ArgumentParser(description='Abstracts data analysis into user functions')
	print(sys.argv)	
	print("parsing arguments")
	myParser = argparse.ArgumentParser(description='Abstracts data analysis into user functions')
		
	
	myParser.add_argument('-f','--fileName',help='fileName',default="None")
	#myParser.add_argument('-dn','--group names',help='fileName',default="None")
	#myParser.add_argument('-sd','--group names',help='show data with group name',default="None")
	
	myArguments = myParser.parse_args()

	main(myArguments.fileName)
