from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vntxvn = Factor("vntxvn", ["opt", "vvvkf"])
hiknfi = Factor("hiknfi", ["ojyy", "wry"])
dsr = Factor("dsr", ["dpl", "cup"])
cdb = Factor("cdb", ["tlxy", "fibldj"])
brtxn = Factor("brtxn", ["zrkqjj", "mpkne"])
mrmoz = Factor("mrmoz", ["uozgu", "kkur"])
jbghdj = Factor("jbghdj", ["ycb", "jom"])

### EXPERIMENT
design=[vntxvn,hiknfi,dsr,cdb,brtxn,mrmoz,jbghdj]
crossing=[[vntxvn,hiknfi,dsr,cdb,brtxn,mrmoz,jbghdj]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_7"))
### END