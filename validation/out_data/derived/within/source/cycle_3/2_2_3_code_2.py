from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
biu = Factor("biu", ["sassd","gotujg","elrdw","umju","kdzoug"])
fva = Factor("fva", ["sassd","gotujg","elrdw","umju","kdzoug"])
xpdbm = Factor("xpdbm", ["sassd","gotujg","elrdw","umju","kdzoug"])
def is_zaab_btyx(biu, fva, xpdbm):
    return biu != xpdbm and biu == fva
def is_zaab_mbxq(biu, fva, xpdbm):
    return not is_zaab_btyx(biu, fva, xpdbm)
zaab= Factor("zaab", [DerivedLevel("btyx", WithinTrial(is_zaab_btyx, [biu, fva, xpdbm])), DerivedLevel("mbxq", WithinTrial(is_zaab_mbxq, [biu, fva, xpdbm]))])

design=[biu,fva,xpdbm,zaab]
crossing=[zaab]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
