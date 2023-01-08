from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nzl = Factor("nzl", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
xmiax = Factor("xmiax", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
vtzuv = Factor("vtzuv", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
def is_sealv_hpwaa(nzl, xmiax, vtzuv):
    return nzl[0] != vtzuv[-1] or nzl[-1] != xmiax[0]
def is_sealv_sryzex(nzl, xmiax, vtzuv):
    return not is_sealv_hpwaa(nzl, xmiax, vtzuv)
sealv = Factor("sealv", [DerivedLevel("hpwaa", Transition(is_sealv_hpwaa, [nzl, xmiax, vtzuv])), DerivedLevel("sryzex", Transition(is_sealv_sryzex, [nzl, xmiax, vtzuv]))])

design=[nzl,xmiax,vtzuv,sealv]
crossing=[sealv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END