from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
g94nw82jbB=Level("{haV",2)
VBa5lm=Factor("YE<",["YBZJBxV","PDS","WJHuH|rDXHnHUe","hgdgZyj","UJZ",'Rue',g94nw82jbB,"exaZ"])
OrjRR08GwD=Factor("BTKTWe@kyCgvN",["}pY",'XoLR',"rvsjPXCGcnqdgg",Level("eFNXMVmtGQYl",4),"qzLkbpGUUwd",'^efYWfnP',"ssmIXo"])

### EXPERIMENT
design=[VBa5lm,OrjRR08GwD]
crossing=[VBa5lm,OrjRR08GwD]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2_1"))
### END