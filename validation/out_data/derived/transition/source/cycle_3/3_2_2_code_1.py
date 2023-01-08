from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ebrckx = Factor("ebrckx", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
qfzure = Factor("qfzure", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
jgvfzo = Factor("jgvfzo", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
def uwxtd(ebrckx, jgvfzo, qfzure):
     return jgvfzo[-1] == ebrckx[0] and ebrckx[-1] != qfzure[0]
def xtvd(ebrckx, jgvfzo, qfzure):
     return jgvfzo[-1] != ebrckx[0] and ebrckx[-1] == qfzure[0]
def ywuhoz(ebrckx, jgvfzo, qfzure):
     return (not uwxtd(ebrckx, jgvfzo, qfzure)) and (not ebrckx[-1] == qfzure[0])
rhpm = DerivedLevel("bahnt", Transition(uwxtd, [ebrckx, qfzure, jgvfzo]))
iye = DerivedLevel("ezdu", Transition(xtvd, [ebrckx, qfzure, jgvfzo]))
hgccu = DerivedLevel("atwd", Transition(ywuhoz, [ebrckx, qfzure, jgvfzo]))
yvdgi = Factor("lfako", [rhpm, iye, hgccu])

### EXPERIMENT
design=[ebrckx,qfzure,jgvfzo,yvdgi]
crossing=[yvdgi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END