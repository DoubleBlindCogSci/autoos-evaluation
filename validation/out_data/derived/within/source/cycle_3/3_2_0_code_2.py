from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
johhmd = Factor("johhmd", ["yohuh","cyvo","tyagv","onjrj","srbbj","trip","bjozvy"])
uujh = Factor("uujh", ["klxyf","jppce","tayjhy","awitqq","hyvn","sgbw","ejtfc"])
def is_pttdar_yvu(johhmd, uujh):
    return johhmd == "srbbj"
def is_pttdar_wnxvg(johhmd, uujh):
    return johhmd != "srbbj" and uujh == "hyvn"
def is_pttdar_wevh(johhmd, uujh):
    return not (is_pttdar_yvu(johhmd, uujh) or is_pttdar_wnxvg(johhmd, uujh))
pttdar= Factor("pttdar", [DerivedLevel("yvu", WithinTrial(is_pttdar_yvu, [johhmd, uujh])), DerivedLevel("wnxvg", WithinTrial(is_pttdar_wnxvg, [johhmd, uujh])), DerivedLevel("wevh", WithinTrial(is_pttdar_wevh, [johhmd, uujh]))])

design=[johhmd,uujh,pttdar]
crossing=[pttdar]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
