from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jfmjpo = Factor("jfmjpo", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
krk = Factor("krk", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
ktn = Factor("ktn", ["dffhaf","atlfu","nqg","frr","kapl","xoopg"])
def is_faobo_uqcsr(jfmjpo, krk, ktn):
    return jfmjpo[-3] == ktn[-1] and jfmjpo[-1] != krk[-3]
def is_faobo_nrzqy(jfmjpo, krk, ktn):
    return ktn[-1] != jfmjpo[-3] and krk[-3] == jfmjpo[-1]
def is_faobo_bzlj(jfmjpo, krk, ktn):
    return not (is_faobo_uqcsr(jfmjpo, krk, ktn) or is_faobo_nrzqy(jfmjpo, krk, ktn))
faobo= Factor("faobo", [DerivedLevel("uqcsr", Window(is_faobo_uqcsr, [jfmjpo, krk, ktn], 4, 1)), DerivedLevel("nrzqy", Window(is_faobo_nrzqy, [jfmjpo, krk, ktn], 4, 1)), DerivedLevel("bzlj", Window(is_faobo_bzlj, [jfmjpo, krk, ktn], 4, 1))])

design=[jfmjpo,krk,ktn,faobo]
crossing=[faobo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
