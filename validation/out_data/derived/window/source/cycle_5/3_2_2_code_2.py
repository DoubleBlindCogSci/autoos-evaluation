from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eov = Factor("eov", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
jryyb = Factor("jryyb", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
fnan = Factor("fnan", ["fivo","ryik","urca","ghfive","lfyir","hbzi","xvedsc","hetd"])
def is_owcv_qfcwn(eov, jryyb, fnan):
    return eov[-1] == jryyb[0] and eov[0] != fnan[-1]
def is_owcv_tvzgy(eov, jryyb, fnan):
    return jryyb[0] != eov[-1] and fnan[-1] == eov[0]
def is_owcv_pgdgge(eov, jryyb, fnan):
    return not (is_owcv_qfcwn(eov, jryyb, fnan) or is_owcv_tvzgy(eov, jryyb, fnan))
owcv = Factor("owcv", [DerivedLevel("qfcwn", Window(is_owcv_qfcwn, [eov, jryyb, fnan], 2, 1)), DerivedLevel("tvzgy", Window(is_owcv_tvzgy, [eov, jryyb, fnan], 2, 1)), DerivedLevel("pgdgge", Window(is_owcv_pgdgge, [eov, jryyb, fnan], 2, 1))])

design=[eov,jryyb,fnan,owcv]
crossing=[owcv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END