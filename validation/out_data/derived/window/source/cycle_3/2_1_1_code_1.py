from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ttak = Factor("ttak", ["klvnuk","deca","xeqi","oegdzv","ntqt"])
def xeck(ttak):
    return ttak[0] != "klvnuk" and ttak[-1] == "xeqi"
def aimzl(ttak):
    return not (ttak[0] != "klvnuk") or not (ttak[0] == "xeqi")
degp = DerivedLevel("pavhzi", Window(xeck, [ttak],2,1))
zxaav = DerivedLevel("typxqe", Window(aimzl, [ttak],2,1))
xvrr = Factor("hrl", [degp, zxaav])

### EXPERIMENT
design=[ttak,xvrr]
crossing=[xvrr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END