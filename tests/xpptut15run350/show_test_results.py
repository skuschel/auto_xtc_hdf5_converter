from pylab import *
import h5py

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

file_name = "xpptut15run350.h5"
my_hdf5_object = h5py.File(file_name,'r')

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

my_key = [i for i in my_dict if 'sec1457995403' in i]

imshow(my_dict[my_key[0]])
clim(2400,2600)
show()
