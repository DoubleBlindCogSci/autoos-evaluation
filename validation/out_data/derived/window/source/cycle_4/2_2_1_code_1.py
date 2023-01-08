from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
sdsksb = Factor("sdsksb", ["eyqoh","mkgnl","osg","gum","mlgp","syfvu","wtjgfi"])
mlrmj = Factor("mlrmj", ["dyfmow","xadjr","jqukpy","eapo","hgp","ugqgfd","hiarx"])
def fnkt(sdsksb, mlrmj):
    return sdsksb[-3] != "eyqoh" and mlrmj[-1] == "xadjr"
def sxqbhj(sdsksb,mlrmj):
    return not fnkt(sdsksb, mlrmj)
nkhz = Factor("vri", [DerivedLevel("bsene", Window(fnkt, [sdsksb, mlrmj],4,1)), DerivedLevel("efsxc", Window(sxqbhj, [sdsksb, mlrmj],4,1))])
### EXPERIMENT
design=[sdsksb,mlrmj,nkhz]
crossing=[nkhz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END