from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qqctd = Factor("qqctd", ["dnhr","vwlutu","erpx","aybjto","cru","vyz","nddsz"])
def tesmu(qqctd):
    return qqctd[-2] == "aybjto" and qqctd[0] == "vwlutu"
def pnv(qqctd):
    return qqctd[-2] != "aybjto" or not (qqctd[0] == "vwlutu")
wki = DerivedLevel("ugeme", Window(tesmu, [qqctd],3,1))
bdr = DerivedLevel("algua", Window(pnv, [qqctd],3,1))
avow = Factor("ecx", [wki, bdr])

### EXPERIMENT
design=[qqctd,avow]
crossing=[avow]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END