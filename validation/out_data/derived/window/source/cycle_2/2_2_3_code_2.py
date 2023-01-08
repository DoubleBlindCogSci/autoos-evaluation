from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ydckd= Factor("ydckd", ["augs","eozzc","ezdw","kvuoan","kmosuf"])
frj= Factor("frj", ["rcqr","tuxwtk","ixn","xxoysb","kitwv","zldb","zeg"])
def is_ckfq_vbsggr(ydckd, frj):
    return ydckd[-2] == "ezdw" and frj[0] == "rcqr"
def is_ckfq_qdpq(ydckd, frj):
    return not is_ckfq_vbsggr(ydckd, frj)
ckfq= Factor("ckfq", [DerivedLevel("vbsggr", Window(is_ckfq_vbsggr, [ydckd, frj], 3, 1)), DerivedLevel("qdpq", Window(is_ckfq_qdpq, [ydckd, frj], 3, 1))])

design=[ydckd,frj, ckfq]
crossing=[ckfq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
