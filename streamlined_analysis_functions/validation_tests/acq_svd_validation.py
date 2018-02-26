#%matplotlib
acqiris_alias="ACQ1"
eigen_basis_file = "eigen_traces.h5"
experiment_name = "amoe7615"
run_number = "201"
channel_number="ch1"
####################
#####################

my_eigen_basis = h5py.File(eigen_basis_file)
eig_bas = array(my_eigen_basis['summary/nonMeaningfulCoreNumber0/'+acqiris_alias+'/'+channel_number+'/norm_eigen_wave_forms'])
#eig_bas = array(my_eigen_basis['summary/nonMeaningfulCoreNumber0/Acq01/'+channel_number+'/eigen_wave_forms'])
#eig_bas = array([eig_bas[i]/sum(eig_bas[i]**2)**0.5 for i in arange(len(eig_bas))])
import psana
my_data_source = psana.MPIDataSource("exp="+experiment_name+":run="+run_number+":smd")
acq_det_obj = psana.Detector(acqiris_alias)
my_enum_events = enumerate(my_data_source.events())
for evt_num,this_event in my_enum_events:
    if evt_num>100:
        break
my_index=argmax((this_event.get(psana.EventId).fiducials() == my_dict['fiducials']).astype(int))
plot(acq_det_obj(this_event)[0][1]-mean(acq_det_obj(this_event)[0][1][:300]))

plot(acq_det_obj(this_event)[0][1]-mean(acq_det_obj(this_event)[0][1][:300]))
plot(dot(my_dict[acqiris_alias+'/'+channel_number+'/weightings'][my_index], eig_bas),'r.')
#plot(dot(my_dict[acqiris_alias+'/'+channel_number+'/weightings'][my_index-1], eig_bas),'r.')
#plot(dot(my_dict[acqiris_alias+'/'+channel_number+'/weightings'][my_index+1], eig_bas),'r.')

