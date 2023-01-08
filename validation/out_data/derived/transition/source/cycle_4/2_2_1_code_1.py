from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yjvend = Factor("yjvend", ["daxgeh","ptvxz","fhkxo","orc","xdufc"])
wlhhi = Factor("wlhhi", ["zhg","vfvhl","nlidm","pudexk","krbx"])
def neoul(yjvend, wlhhi):
    return yjvend[0] == "orc" and wlhhi[-1] == "krbx"
def rdr(yjvend,wlhhi):
    return not (yjvend[0] == "orc") or wlhhi[-1] != "krbx"
jth = DerivedLevel("uic", Transition(neoul, [yjvend, wlhhi]))
fjrfea = DerivedLevel("hsiyw", Transition(rdr, [yjvend, wlhhi]))
feuktd = Factor("yzdw", [jth, fjrfea])

### EXPERIMENT
design=[yjvend,wlhhi,feuktd]
crossing=[feuktd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END