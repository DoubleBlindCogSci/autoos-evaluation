from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fmq = Factor("fmq", ["cvsb","yerlnd","bbnyn","jfg","ivw"])
def is_kkvmaj_xldt(fmq):
    return fmq != "cvsb" and fmq != "yerlnd"
def is_kkvmaj_fxq(fmq):
    return not is_kkvmaj_xldt(fmq)
kkvmaj = Factor("kkvmaj", [DerivedLevel("xldt", WithinTrial(is_kkvmaj_xldt, [fmq])), DerivedLevel("fxq", WithinTrial(is_kkvmaj_fxq, [fmq]))])

design=[fmq,kkvmaj]
crossing=[kkvmaj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END