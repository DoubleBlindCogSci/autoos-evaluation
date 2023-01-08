from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nzl = Factor("nzl", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
xmiax = Factor("xmiax", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
vtzuv = Factor("vtzuv", ["squy","tltgoo","cjbwo","zwbruy","zxek","tps","xmsl"])
def eosems(nzl, vtzuv, xmiax):
    return nzl[0] != vtzuv[-1] or nzl[-1] != xmiax[0]
def wjm(nzl, vtzuv, xmiax):
    return not (nzl[0] != vtzuv[-1]) and nzl[-1] == xmiax[0]
ynazla = Factor("sealv", [DerivedLevel("hpwaa", Transition(eosems, [nzl, xmiax, vtzuv])), DerivedLevel("sryzex", Transition(wjm, [nzl, xmiax, vtzuv]))])
### EXPERIMENT
design=[nzl,xmiax,vtzuv,ynazla]
crossing=[ynazla]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END