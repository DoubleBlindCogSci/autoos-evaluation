from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tGVS9=Factor('Vp>JpTcEPpTvQ6',[Level("Exbj",4),"IaU",Level('WS0',4)])
Jl8nIEW3WM=['PJvPW','us~!@xvF',Level('I|?pdoQyWNXNO',2)]
fZ6LD=Factor('sKXkOx',Jl8nIEW3WM)

### EXPERIMENT
design=[tGVS9,fZ6LD]
crossing=[tGVS9,fZ6LD]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END