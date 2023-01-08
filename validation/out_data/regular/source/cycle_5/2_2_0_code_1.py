from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
L4dx=["Ub#",'INmFAsImU']
RbI6ma=Factor("QzCcJJyQWm&jh",L4dx)
_DiJXy=Factor('<He[oHGjgzz',['uHx 5wkPFW',';s 4MSSLBSac'])

### EXPERIMENT
design=[RbI6ma,_DiJXy]
crossing=[RbI6ma,_DiJXy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END