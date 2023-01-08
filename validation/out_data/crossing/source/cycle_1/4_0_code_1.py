from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hhl = Factor("hhl", ["kjorlx", "jdpo"])
uxzmw = Factor("uxzmw", ["fgmu", "mcbni"])
jbda = Factor("jbda", ["hfh", "ioo"])
rspui = Factor("rspui", ["ydh", "efenx"])
pcbhls = Factor("pcbhls", ["givo", "iejky"])
zij = Factor("zij", ["ncecmx", "wqeey"])
qku = Factor("qku", ["dbma", "hcmgac"])

### EXPERIMENT
design=[hhl,uxzmw,jbda,rspui,pcbhls,zij,qku]
crossing=[[hhl],[uxzmw,jbda,rspui,pcbhls],[zij],[qku],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0"))
### END