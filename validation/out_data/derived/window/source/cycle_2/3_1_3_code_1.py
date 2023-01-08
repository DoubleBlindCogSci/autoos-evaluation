from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mcfe = Factor("mcfe", ["cjd","pdhx","gxwuy","kwmu","jjuu","pzqea","llbj"])
def krwuj(mcfe):
     return mcfe[-3] == "jjuu" and not mcfe[0] == "jjuu"
def spwdju(mcfe):
     return mcfe[-3] != "jjuu" and  mcfe[0] == "cjd"
def bix(mcfe):
     return (not mcfe[-3] == "jjuu") and (mcfe[0] != "cjd")
unki = Factor("ewfej", [DerivedLevel("jozju", Window(krwuj, [mcfe],4,1)), DerivedLevel("tozb", Window(spwdju, [mcfe],4,1)),DerivedLevel("qpbcog", Window(bix, [mcfe],4,1))])
### EXPERIMENT
design=[mcfe,unki]
crossing=[unki]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END