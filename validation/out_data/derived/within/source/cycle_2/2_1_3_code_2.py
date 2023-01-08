from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ijpw= Factor("ijpw", ["iya","pjrywo","niuvji","cqy","mmcg"])
def is_cqzazp_jxot(ijpw):
    return ijpw != "iya"
def is_cqzazp_khyach(ijpw):
    return not is_cqzazp_jxot(ijpw)
cqzazp= Factor("cqzazp", [DerivedLevel("jxot", WithinTrial(is_cqzazp_jxot, [ijpw])), DerivedLevel("khyach", WithinTrial(is_cqzazp_khyach, [ijpw]))])

design=[ijpw, cqzazp]
crossing=[cqzazp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
