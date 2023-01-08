from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ctsfA7q='jdhGrna'
NwWK4Z3k=Factor("H#ymIW:&",[Level('qWFHHX:jFVOvX',3),'rNif',"TEFwkWzmYBth",ctsfA7q,Level('JVz',7),'2t&coV#X','ahT','FoyjlRy}Q~r'])

### EXPERIMENT
design=[NwWK4Z3k]
crossing=[NwWK4Z3k]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/7_1_0"))
### END