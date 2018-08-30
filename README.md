# auto_xtc_hdf5_converter

This package separates the science analysis from the psana overhead when converting xtc to hdf5 files.

## Examples
Examples can be found in the 'tests' folder.  They use the publicly available practice data
https://confluence.slac.stanford.edu/display/PSDM/Publicly+Available+Practice+Data

run the test.sh scripts to execute the example. (some of them require "X forwarding")


The purpose of the examples in this repository is to allow users to copy one of the test directories, tweak the files, and start analyzing their own data.
The test.sh scripts found in directories starting with 'xpp' can be run directly.
Make sure to ssh to a psana machine before trying to run these scripts.
The examples have a soft link to analysisFunctions.py in the config directory. The soft link can be removed and replaced with the actual file
### more detailed descriptions

xpptut15run350 demonstrates how to retrieve 'slow camera' data.

xpptut15run360 demonstrates how to retrive 'full vertically binned' data.

xpptut15run420 demonstrates how to retrive 'arrival time tool monitor' data. (the hdf5 key is 'attm_opal')

xpptut15run440 demonstrates how to retrive and calculate low rank approximations( i.e. cludge implementation of iterative svd) of digitizer data and how to reconstruct the data. This procedure is somewhat involved, but solves a number of issues including the memory problem of writing millions full digitizer waveforms to disk.)  The various plots that pop up need to closed for this script to continue.

### how to tweak example files
before trying to apply this package to your data, copy and try and tweak the example directories.  (i.e. The directories in 'tests' starting with 'xpp')

The files that need to be modified are the config/analysis.cfg and config/analysisFunctions.py.

the analysis.cfg is a set of columns that tells the auto_xtc_extractor how to analyze xtc data coming.

The 1st column is the devices 'DAQ'     alias (e.g. SxrEndstation.0:Acqiris.1,Acq01). 
The 2nd column is the devices 'psana'   alias (e.g. Acq01). 
The 3rd column is the is empty
The 4th column is the devices 'auto_xtc_extractor' alias (e.g. Acq01).  This alias is used as the base hdf5 key for the hdf5 file written to disk.

The 5th column in the name of a function that appears in analysisFunctions.py. This function is applied to the data coming from the detector specified in columns 1 and 2. The results from this function are a dictionary that gets written to hdf5 on a event-by-event (i.e. per x-ray pulse) basis.

The 6th column also tells the auto_xtc_extractor which function to use. But these functions accumulate data and write once after all the events are processed.  This is used for summing up all the images from a detector or reading out 'slow camera' data that only appears every several thousand events.

try commenting out some lines in analysis.cfg or and tweak some functions in analysisFunctions.py.

## Creating own config folders

to create your own config run the command below

../../analysisDetectorConfigGenerator.py -e sxrlr0116 -r 35

where sxrlr0116 and 35 can be replaced with any experiment and run

in a new directory under test.

## Quick Start

</pre>$ PATH ="$PATH:/reg/g/psdm/sw/hutch/sxd/auto_xtc_hdf5_converter" </pre>

navigate to a directory where you'd like to do the analysis.

</pre>$ analysisDetectorConfigGenerator.py -e xpptut15 -r 280 </pre>

this line of code generates a config directory with files analysis.cfg and analysisFunctions.py.


</pre>$ psanaXtcDataExtractor.py -e xpptut15 -r 280 -t </pre>

this line converts the xtc file to an hdf5 file called xpptut15run280.h5.

### More involved quick start

The example above only gets a small portion of the xtc data. to get more data, the analysis.cfg and analysisFunctions.py files in the config directory need to be edited. (instructions forth coming)

### Usage

usage: psanaXtcDataExtractor.py [-h] [-e EXP] [-r RUN] [-c CONFIGFILE]
                                [-hd5 HD5FILE] [-t] [-td TTDEVICE]
                                [-tc TTCODE] [-s START] [-f FINAL]

Abstracts data analysis into user functions

optional arguments:

  -h, --help            show this help message and exit

  -e EXP, --exp EXP     the experiment name

  -r RUN, --run RUN     the run number to use when running offline

  -c CONFIGFILE, --configFile CONFIGFILE
                        the config file to read from

  -hd5 HD5FILE, --hd5File HD5FILE
                        extension of the small data file to write to.
                        typically a,b or c

  -t, --testSample      only take a small set of data for testing

  -td TTDEVICE, --ttDevice TTDEVICE
                        device to use for getting time tool

  -tc TTCODE, --ttCode TTCODE
                        event code to identify by kick

  -s START, --start START
                        skips until starting event reached

  -f FINAL, --final FINAL
                        up to final event

