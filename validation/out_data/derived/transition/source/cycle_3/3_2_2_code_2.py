from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ebrckx = Factor("ebrckx", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
qfzure = Factor("qfzure", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
jgvfzo = Factor("jgvfzo", ["prun","oofad","sodki","fcgvjo","edox","ydn","mfi","pfjr"])
def is_lfako_bahnt(ebrckx, qfzure, jgvfzo):
    return jgvfzo[-1] == ebrckx[0] and ebrckx[-1] != qfzure[0]
def is_lfako_ezdu(ebrckx, qfzure, jgvfzo):
    return jgvfzo[-1] != ebrckx[0] and ebrckx[-1] == qfzure[0]
def is_lfako_atwd(ebrckx, qfzure, jgvfzo):
    return jgvfzo[-1] != ebrckx[0] and ebrckx[-1] != qfzure[0]
lfako= Factor("lfako", [DerivedLevel("bahnt", Transition(is_lfako_bahnt, [ebrckx, qfzure, jgvfzo])), DerivedLevel("ezdu", Transition(is_lfako_ezdu, [ebrckx, qfzure, jgvfzo])), DerivedLevel("atwd", Transition(is_lfako_atwd, [ebrckx, qfzure, jgvfzo]))])

design=[ebrckx,qfzure,jgvfzo,lfako]
crossing=[lfako]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
