from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sdsksb = Factor("sdsksb", ["eyqoh","mkgnl","osg","gum","mlgp","syfvu","wtjgfi"])
mlrmj = Factor("mlrmj", ["dyfmow","xadjr","jqukpy","eapo","hgp","ugqgfd","hiarx"])
def is_vri_bsene(sdsksb, mlrmj):
    return sdsksb[-3] != "eyqoh" and mlrmj[-1] == "xadjr"
def is_vri_efsxc(sdsksb, mlrmj):
    return not is_vri_bsene(sdsksb, mlrmj)
vri= Factor("vri", [DerivedLevel("bsene", Window(is_vri_bsene, [sdsksb, mlrmj], 4, 1)), DerivedLevel("efsxc", Window(is_vri_efsxc, [sdsksb, mlrmj], 4, 1))])

design=[sdsksb,mlrmj,vri]
crossing=[vri]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END