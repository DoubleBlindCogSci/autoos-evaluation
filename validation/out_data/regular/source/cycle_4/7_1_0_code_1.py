from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Sn_uTt2d="teUZsTZAI"
HYU6L=Factor('ZMT<HDPrv',['IEM(0~QoZ',"AmiJ(HkuBB",'KjNIzZMgR','yQNLkC8',"VW$xUUt",Sn_uTt2d,Level('w(FEXfsSr6KU|',1),'BcTS'])

### EXPERIMENT
design=[HYU6L]
crossing=[HYU6L]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1_0"))
### END