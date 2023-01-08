from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bsy= Factor("bsy", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
nopd= Factor("nopd", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
fhq= Factor("fhq", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
def is_nsaqy_xkn(bsy, nopd):
    return bsy[0] == nopd[-3]
def is_nsaqy_bxvp(bsy, nopd, fhq):
    return bsy[0] != nopd[-3] and fhq[0] == bsy[-3]
def is_nsaqy_ylwc(bsy, nopd, fhq):
    return not (is_nsaqy_xkn(bsy, nopd) or is_nsaqy_bxvp(bsy, nopd, fhq))
nsaqy= Factor("nsaqy", [DerivedLevel("xkn", Window(is_nsaqy_xkn, [bsy, nopd], 4, 1)), DerivedLevel("bxvp", Window(is_nsaqy_bxvp, [bsy, nopd, fhq], 4, 1)), DerivedLevel("ylwc", Window(is_nsaqy_ylwc, [bsy, nopd, fhq], 4, 1))])

design=[bsy,nopd,fhq,nsaqy]
crossing=[nsaqy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
