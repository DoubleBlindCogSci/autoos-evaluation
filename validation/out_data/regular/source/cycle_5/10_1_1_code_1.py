from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xuA1iTJs0=Factor("@tlmBMqKyTQpk",['LSk','aU{y>>Kz','5AK',"ggttkmK5gLyw",'?YDNXax@P','sjDZylk',"6goF",Level('y1IloF:khMSw5T',2),"ZofSvJE8p",'6|UdTVw'])

### EXPERIMENT
design=[xuA1iTJs0]
crossing=[xuA1iTJs0]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/10_1_1"))
### END