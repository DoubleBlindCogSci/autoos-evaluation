from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qozaj = Factor("qozaj", ["npbmju","zby","jjgc","aje","vmxii","akl"])
def cerkyv(qozaj):
    return qozaj[-1] != "npbmju" and qozaj[-3] != "aje"
def ibu(qozaj):
    return qozaj[-1] == "npbmju" or not (qozaj[-3] != "aje")
djt = DerivedLevel("purf", Window(cerkyv, [qozaj],4,1))
exf = DerivedLevel("nkjhjd", Window(ibu, [qozaj],4,1))
bbq = Factor("mhjwrc", [djt, exf])

### EXPERIMENT
design=[qozaj,bbq]
crossing=[bbq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END