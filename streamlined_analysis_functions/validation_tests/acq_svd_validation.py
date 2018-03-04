#%matplotlib
acqiris_alias="Acq01"
eigen_basis_file = "eigen_traces.h5"
experiment_name = "sxrlr1516"
run_number = "21"
channel_number=2
event_number = 1440
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
plot(acq_det_obj(this_event)[0][channel_number]-mean(acq_det_obj(this_event)[0][channel_number][:300]))

plot(acq_det_obj(this_event)[0][channel_number]-mean(acq_det_obj(this_event)[0][channel_number][:300]))
plot(dot(my_dict[acqiris_alias+'/ch'+str(channel_number)+'/weightings'][my_index], eig_bas),'r.')
show()
