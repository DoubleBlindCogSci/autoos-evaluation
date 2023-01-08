from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DZHINRsjzV=Factor("fiFAZYEF7",[Level('n;u{',10),Level('}JStvuEbR',6),Level('ZVM',3),'Oq z^{KPRkVf'])
vQsC_=Factor('K MYI4SMfSMnLr',[Level("YyV~klXy!K8Xf",5),Level('G[N%:vgGnTw',10),"yXrWqW}4[",'|Pj'])

### EXPERIMENT
design=[DZHINRsjzV,vQsC_]
crossing=[DZHINRsjzV,vQsC_]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_1"))
### END