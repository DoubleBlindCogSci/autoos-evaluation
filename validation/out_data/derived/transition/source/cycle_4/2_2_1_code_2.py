from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yjvend = Factor("yjvend", ["daxgeh","ptvxz","fhkxo","orc","xdufc"])
wlhhi = Factor("wlhhi", ["zhg","vfvhl","nlidm","pudexk","krbx"])
def is_yzdw_uic(yjvend, wlhhi):
    return yjvend[0] == "orc" and wlhhi[0] == "krbx"
def is_yzdw_hsiyw(yjvend, wlhhi):
    return not is_yzdw_uic(yjvend, wlhhi)
yzdw= Factor("yzdw", [DerivedLevel("uic", Transition(is_yzdw_uic, [yjvend, wlhhi])), DerivedLevel("hsiyw", Transition(is_yzdw_hsiyw, [yjvend, wlhhi]))])

design=[yjvend,wlhhi,yzdw]
crossing=[yjvend]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END