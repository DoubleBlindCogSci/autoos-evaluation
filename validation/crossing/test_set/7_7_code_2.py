from sweetpea import *
import os
_dir=os.path.dirname(__file__)
vntxvn = Factor("vntxvn", ["opt", "vvvkf"])
hiknfi = Factor("hiknfi", ["ojyy", "wry"])
dsr = Factor("dsr", ["dpl", "cup"])
cdb = Factor("cdb", ["tlxy", "fibldj"])
brtxn = Factor("brtxn", ["zrkqjj", "mpkne"])
mrmoz = Factor("mrmoz", ["uozgu", "kkur"])
jbghdj = Factor("jbghdj", ["ycb", "jom"])
constraints = []
crossing = [vntxvn, hiknfi, dsr, cdb, brtxn, mrmoz, jbghdj]


design=[vntxvn,hiknfi,dsr,cdb,brtxn,mrmoz,jbghdj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_7"))

### END