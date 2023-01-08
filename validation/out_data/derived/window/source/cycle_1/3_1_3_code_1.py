from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tqywwe = Factor("tqywwe", ["jep","givaf","dshe","hvdbkc","antde","mqan","ceb"])
def uhmcb(tqywwe):
     return "dshe" == tqywwe[-1]
def jeop(tqywwe):
     return "givaf" == tqywwe[-2]
def mko(tqywwe):
     return (not tqywwe[-1] == "dshe") and (not tqywwe[-2] == "givaf")
kay = Factor("xcic", [DerivedLevel("lfli", Window(uhmcb, [tqywwe],3,1)), DerivedLevel("fovsd", Window(jeop, [tqywwe],3,1)),DerivedLevel("sfo", Window(mko, [tqywwe],3,1))])
### EXPERIMENT
design=[tqywwe,kay]
crossing=[kay]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END