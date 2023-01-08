from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
vkjko = Factor("vkjko", ["fga", "pdoq"])
wgrgtc = Factor("wgrgtc", ["bbwayz", "tmthev"])
wewe = Factor("wewe", ["fga", "pdoq"])
jkhd = Factor("jkhd", ["bbwayz", "tmthev"])
oir = Factor("oir", ["bjpq", "sfjahf"])
def mqob (oir, jkhd):
    return oir == jkhd
def ubgfkw (oir, jkhd):
    return not mqob(oir, jkhd)
eivlb = Factor("eivlb", [DerivedLevel("irho", WithinTrial(mqob, [oir, jkhd])), DerivedLevel("hjbpis", WithinTrial(ubgfkw, [oir, jkhd]))])
design=[eivlb,vkjko,wgrgtc,wewe,jkhd,oir]
constraints=[MinimumTrials(26)]
crossing=[wgrgtc,eivlb]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_1"))
