from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rlfgp = Factor("rlfgp", ["uwwu","nnviqh","adovs","lkq","ngeuv","fweki","zofa","nmu"])
def is_lgjokh_hhxn(rlfgp):
    return rlfgp[0] == "lkq" and rlfgp[-1] != "fweki"
def is_lgjokh_nlh(rlfgp):
    return rlfgp[0] != "lkq" and rlfgp[-1] == "fweki"
def is_lgjokh_tyuxva(rlfgp):
    return not (is_lgjokh_hhxn(rlfgp) or is_lgjokh_nlh(rlfgp))
lgjokh= Factor("lgjokh", [DerivedLevel("hhxn", Transition(is_lgjokh_hhxn, [rlfgp])), DerivedLevel("nlh", Transition(is_lgjokh_nlh, [rlfgp])), DerivedLevel("tyuxva", Transition(is_lgjokh_tyuxva, [rlfgp]))])

design=[rlfgp,lgjokh]
crossing=[lgjokh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
