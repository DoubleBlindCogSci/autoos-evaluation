from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
thXjI6avFQi=Factor('JSFI',["GM]pIPOG3y","RuyAPVcjS9w","UUJeR}mTelsSt",Level('} AXX',4),"ArmhRNG"])
eHN8f='DnHu^H'
x5oUmlLR=Factor("YOdrl%w",['OQPCX{~DyQ',eHN8f,'Zejt',"9ALXA{",'tjlzFr$ie','vMHWaCbpJ A'])

### EXPERIMENT
design=[thXjI6avFQi,x5oUmlLR]
crossing=[thXjI6avFQi,x5oUmlLR]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_0"))
### END