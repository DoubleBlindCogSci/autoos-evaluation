from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
UA9tJ='@UfGUQ#oOE'
C37H1Z6hH4=Factor('qZiA&rdFb!',[Level('dhZz',1),"W]HTNkuTPPauH_",'dRSUOQN',"H?2cPcLFghVTlv",'O%aCsphHO',UA9tJ])
gb57VRKKaDM="jd7mGapM"
UPi_nZl03=Factor('BYbmeW]JhESi',['Izhtx',gb57VRKKaDM,"0HVETiRa","AZCw8vbYXO",' fdafalQj','FLoZQfQEDLnC'])
MH7XCjFO=Factor('F GXAnimmff',['[VE',Level("d:CFFaGGBtd",3),"UeKS","lOs>ojr%eMbJ","1X1CnPsI>I1eeg"])

### EXPERIMENT
design=[C37H1Z6hH4,UPi_nZl03,MH7XCjFO]
crossing=[C37H1Z6hH4,UPi_nZl03,MH7XCjFO]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3_1"))
### END