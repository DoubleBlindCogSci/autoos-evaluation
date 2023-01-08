from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dqCd=['>neZ(xRB',"YfzN","xQTObpzFYMn",'UKKSPSrtiw']
lfMldBpt2T=Factor('kNNU',dqCd)
SuuWtL0hVp=' Fx'
nVafi0=Factor('QnpjG',["NO>","tvPqB{","ISbyAqOADENd v",Level("IqzUUIBUNfCRu",3),SuuWtL0hVp])

### EXPERIMENT
design=[lfMldBpt2T,nVafi0]
crossing=[lfMldBpt2T,nVafi0]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_2_1"))
### END