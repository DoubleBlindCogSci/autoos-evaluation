from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tghaa= Factor("tghaa", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
bbxa= Factor("bbxa", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
yzpsqo= Factor("yzpsqo", ["hmah","iyh","fqxb","zkq","dwrvgs","kpe"])
def is_yemznk_bjpwk(tghaa, bbxa, yzpsqo):
    return yzpsqo == tghaa
def is_yemznk_nzvgd(tghaa, bbxa, yzpsqo):
    return yzpsqo != tghaa and bbxa == tghaa
def is_yemznk_pnkcuy(tghaa, bbxa, yzpsqo):
    return yzpsqo != tghaa and bbxa != tghaa
yemznk= Factor("yemznk", [DerivedLevel("bjpwk", WithinTrial(is_yemznk_bjpwk, [tghaa, bbxa, yzpsqo])), DerivedLevel("nzvgd", WithinTrial(is_yemznk_nzvgd, [tghaa, bbxa, yzpsqo])), DerivedLevel("pnkcuy", WithinTrial(is_yemznk_pnkcuy, [tghaa, bbxa, yzpsqo]))])

design=[tghaa,bbxa,yzpsqo,yemznk]
crossing=[yemznk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
