from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xmm = Factor("xmm", ["czc", "indw"])
cjry = Factor("cjry", ["vyc", "ysdm"])
eymoy = Factor("eymoy", ["djt", "vzndld"])
jkjp = Factor("jkjp", ["zbidzn", "terh"])
yjs = Factor("yjs", ["acnmty", "veoqvv"])

### EXPERIMENT
design=[xmm,cjry,eymoy,jkjp,yjs]
crossing=[[xmm,cjry,eymoy,jkjp],[yjs],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3"))
### END