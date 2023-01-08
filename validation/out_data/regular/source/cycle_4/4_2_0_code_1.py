from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ca2aioVc=Factor('mBCPXKa',['HSAu~','%yzX2{Wok',"TsplnW",'w;tTlmI{N'])
kcZdf=Factor("eMCNJAW",['eHvr@zz4','oZD',Level("cBUXvvi",1),"mclh3qMXRjkzoi"])

### EXPERIMENT
design=[ca2aioVc,kcZdf]
crossing=[ca2aioVc,kcZdf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_0"))
### END