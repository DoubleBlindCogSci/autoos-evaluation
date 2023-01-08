from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
johhmd = Factor("johhmd", ["yohuh","cyvo","tyagv","onjrj","srbbj","trip","bjozvy"])
uujh = Factor("uujh", ["klxyf","jppce","tayjhy","awitqq","hyvn","sgbw","ejtfc"])
def eplv(johhmd, uujh):
     return johhmd == "srbbj"
def akkgpb(johhmd, uujh):
     return "srbbj" != johhmd and  uujh == "hyvn"
def tmaoj(johhmd, uujh):
     return (not eplv(johhmd, uujh)) and (not uujh == "hyvn")
fzl = Factor("pttdar", [DerivedLevel("yvu", WithinTrial(eplv, [johhmd, uujh])), DerivedLevel("wnxvg", WithinTrial(akkgpb, [johhmd, uujh])),DerivedLevel("wevh", WithinTrial(tmaoj, [johhmd, uujh]))])
### EXPERIMENT
design=[johhmd,uujh,fzl]
crossing=[fzl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END