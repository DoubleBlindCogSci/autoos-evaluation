from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
eov = Factor("eov", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
jryyb = Factor("jryyb", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
fnan = Factor("fnan", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
def avqosx(eov, jryyb, fnan):
     return eov[-1] == jryyb[0] and eov[0] != fnan[-1]
def ugqol(eov, jryyb, fnan):
     return jryyb[0] != eov[-1] and fnan[-1] == eov[0]
def gfva(eov, jryyb, fnan):
     return (not eov[-1] == jryyb[0]) and (not ugqol(eov, jryyb, fnan))
emfamx = DerivedLevel("qfcwn", Window(avqosx, [eov, jryyb, fnan],2,1))
epmsqc = DerivedLevel("tvzgy", Window(ugqol, [eov, jryyb, fnan],2,1))
tswodf = DerivedLevel("pgdgge", Window(gfva, [eov, jryyb, fnan],2,1))
nudlrq = Factor("owcv", [emfamx, epmsqc, tswodf])

### EXPERIMENT
design=[eov,jryyb,fnan,nudlrq]
crossing=[nudlrq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END