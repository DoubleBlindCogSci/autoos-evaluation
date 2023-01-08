from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hstuwb = Factor("hstuwb", ["leuc","epe","vtgmh","grktu","lzciwx","slzolh"])
zfln = Factor("zfln", ["ydiyqj","nhj","rld","llh","dnsu","qiwv"])
def xow(hstuwb, zfln):
     return hstuwb[-1] == "slzolh" and not zfln[0] == "ydiyqj"
def apz(hstuwb, zfln):
     return hstuwb[-1] != "slzolh" and zfln[0] == "ydiyqj"
def fqdi(hstuwb, zfln):
     return (not hstuwb[-1] == "slzolh") and (not apz(hstuwb, zfln))
tvzj = Factor("eqm", [DerivedLevel("fbhrc", Transition(xow, [hstuwb, zfln])), DerivedLevel("thwl", Transition(apz, [hstuwb, zfln])),DerivedLevel("ixo", Transition(fqdi, [hstuwb, zfln]))])
### EXPERIMENT
design=[hstuwb,zfln,tvzj]
crossing=[tvzj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END