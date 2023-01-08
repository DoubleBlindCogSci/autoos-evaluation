from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nuh = Factor("nuh", ["jtv","gvgvz","ysog","fzejv","kedcat","zuefq","wwfptp"])
srcbv = Factor("srcbv", ["kizoj","xgiimi","pvqs","mok","rnzppo","pxnav","ugutef"])
def zska(nuh, srcbv):
     return nuh == "zuefq"
def facda(nuh, srcbv):
     return "zuefq" != nuh and  srcbv == "pxnav"
def uaa(nuh, srcbv):
     return (nuh != "zuefq") and (not srcbv == "pxnav")
rkfan = DerivedLevel("egilme", WithinTrial(zska, [nuh, srcbv]))
alr = DerivedLevel("oxv", WithinTrial(facda, [nuh, srcbv]))
gcuw = DerivedLevel("qqmd", WithinTrial(uaa, [nuh, srcbv]))
idasq = Factor("mnjfm", [rkfan, alr, gcuw])

### EXPERIMENT
design=[nuh,srcbv,idasq]
crossing=[idasq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END