from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kX0oWT8=Factor("{%BI_g6XF",['jyii','HZ3Qv '])
HyeFQL=Factor('cEO)VAKx',["p&PLjSRFjie%#1",Level('_{EOfzrFhKw@9R',4)])

### EXPERIMENT
design=[kX0oWT8,HyeFQL]
crossing=[kX0oWT8,HyeFQL]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END