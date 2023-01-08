from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rlfgp = Factor("rlfgp", ["uwwu","nnviqh","adovs","lkq","ngeuv","fweki","zofa","nmu"])
def okoqlj(rlfgp):
     return "lkq" == rlfgp[0] and rlfgp[-1] != "fweki"
def iyheoe(rlfgp):
     return (not "lkq" != rlfgp[0]) and  "fweki" == rlfgp[-1]
def kew(rlfgp):
     return (not okoqlj(rlfgp)) and (rlfgp[-1] != "fweki")
qlx = Factor("lgjokh", [DerivedLevel("hhxn", Transition(okoqlj, [rlfgp])), DerivedLevel("nlh", Transition(iyheoe, [rlfgp])),DerivedLevel("tyuxva", Transition(kew, [rlfgp]))])
### EXPERIMENT
design=[rlfgp,qlx]
crossing=[qlx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END