from sweetpea import *
import os
_dir=os.path.dirname(__file__)
dfhsk = Factor("dfhsk", ["gad", "hho"])
vhitdz = Factor("vhitdz", ["yxb", "jyjk"])
rvjqx = Factor("rvjqx", ["jve", "cctzk"])
mwk = Factor("mwk", ["dbr", "pqrbtz"])
eyzr = Factor("eyzr", ["nnkz", "bckly"])
constraints = []
crossing = [[dfhsk, vhitdz], [rvjqx, mwk], [eyzr]]


design=[dfhsk,vhitdz,rvjqx,mwk,eyzr]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_0"))

### END