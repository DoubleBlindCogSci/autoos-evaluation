from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qzxAodAfG='ccXS2SxY4MQ'
c_nX=Factor('HzG3aYol',["}OLLHVQuFB","Wdas",'iqGaiGASGpm',"Onc",'eNM',qzxAodAfG])

### EXPERIMENT
design=[c_nX]
crossing=[c_nX]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_1"))
### END