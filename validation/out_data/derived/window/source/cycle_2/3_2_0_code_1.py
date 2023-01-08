from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tjqjy = Factor("tjqjy", ["ezrg","lxhb","spwqj","nigrt","hhzjy","eocn"])
tclqkw = Factor("tclqkw", ["scals","ndjw","rxa","hig","qwlv","svyx","ogwjy"])
def jyu(tjqjy, tclqkw):
     return tjqjy[-1] == "lxhb" and tclqkw[-2] != "scals"
def xbf(tjqjy, tclqkw):
     return tjqjy[-1] != "lxhb" and  tclqkw[-2] == "scals"
def lmxyos(tjqjy, tclqkw):
     return (not jyu(tjqjy, tclqkw)) and (not xbf(tjqjy, tclqkw))
svxuq = DerivedLevel("dkytkh", Window(jyu, [tjqjy, tclqkw],3,1))
jwvj = DerivedLevel("vfz", Window(xbf, [tjqjy, tclqkw],3,1))
jncp = DerivedLevel("hizcf", Window(lmxyos, [tjqjy, tclqkw],3,1))
dxgiew = Factor("otzpw", [svxuq, jwvj, jncp])

### EXPERIMENT
design=[tjqjy,tclqkw,dxgiew]
crossing=[dxgiew]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END