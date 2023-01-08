from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pcqefj = Factor("pcqefj", ["cdjnz","lgco","rduahx","fdu","fmy","mcsovj","cmb","cmj"])
def tdcbhh(pcqefj):
     return "lgco" == pcqefj
def jzoumu(pcqefj):
     return "fmy" == pcqefj
def butgov(pcqefj):
     return (not tdcbhh(pcqefj)) and (not jzoumu(pcqefj))
qvnn = DerivedLevel("btv", WithinTrial(tdcbhh, [pcqefj]))
petlzf = DerivedLevel("hvi", WithinTrial(jzoumu, [pcqefj]))
mvhgh = DerivedLevel("hyajkt", WithinTrial(butgov, [pcqefj]))
aek = Factor("dgm", [qvnn, petlzf, mvhgh])

### EXPERIMENT
design=[pcqefj,aek]
crossing=[aek]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END