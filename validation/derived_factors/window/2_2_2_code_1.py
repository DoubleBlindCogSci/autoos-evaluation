from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nftejx = Factor("nftejx", ["slppp","onzvvm","dhzy","syu","sxis"])
zqsk = Factor("zqsk", ["slppp","onzvvm","dhzy","syu","sxis"])
apbr = Factor("apbr", ["slppp","onzvvm","dhzy","syu","sxis"])
def ldsboj(nftejx, apbr, zqsk):
    return nftejx[-2] != apbr[0]
def hrievt(nftejx, apbr, zqsk):
    return not (nftejx[-2] != apbr[0])
upgkr = DerivedLevel("mlr", Window(ldsboj, [nftejx, zqsk, apbr],3,1))
xtihv = DerivedLevel("iypza", Window(hrievt, [nftejx, zqsk, apbr],3,1))
osi = Factor("noe", [upgkr, xtihv])

### EXPERIMENT
design=[nftejx,zqsk,apbr,osi]
crossing=[osi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END