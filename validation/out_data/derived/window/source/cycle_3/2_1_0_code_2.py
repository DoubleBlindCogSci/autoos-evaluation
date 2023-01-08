from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qozaj = Factor("qozaj", ["npbmju","zby","jjgc","aje","vmxii","akl"])
def is_mhjwrc_purf(qozaj):
    return qozaj[-1] != "npbmju" and qozaj[-3] != "aje"
def is_mhjwrc_nkjhjd(qozaj):
    return not is_mhjwrc_purf(qozaj)
mhjwrc= Factor("mhjwrc", [DerivedLevel("purf", Window(is_mhjwrc_purf, [qozaj], 4, 1)), DerivedLevel("nkjhjd", Window(is_mhjwrc_nkjhjd, [qozaj], 4, 1))])

design=[qozaj,mhjwrc]
crossing=[mhjwrc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
