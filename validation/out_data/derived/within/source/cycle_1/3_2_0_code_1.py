from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tghaa = Factor("tghaa", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
bbxa = Factor("bbxa", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
yzpsqo = Factor("yzpsqo", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
def zyv(tghaa, yzpsqo, bbxa):
     return yzpsqo == tghaa
def ukg(tghaa, yzpsqo, bbxa):
     return yzpsqo != tghaa and bbxa == tghaa
def oscft(tghaa, yzpsqo, bbxa):
     return (tghaa != yzpsqo) and (not tghaa == bbxa)
oigxjk = Factor("yemznk", [DerivedLevel("bjpwk", WithinTrial(zyv, [tghaa, bbxa, yzpsqo])), DerivedLevel("nzvgd", WithinTrial(ukg, [tghaa, bbxa, yzpsqo])),DerivedLevel("pnkcuy", WithinTrial(oscft, [tghaa, bbxa, yzpsqo]))])
### EXPERIMENT
design=[tghaa,bbxa,yzpsqo,oigxjk]
crossing=[oigxjk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END