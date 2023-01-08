from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ydckd = Factor("ydckd", ["augs","eozzc","ezdw","kvuoan","kmosuf"])
frj = Factor("frj", ["rcqr","tuxwtk","ixn","xxoysb","kitwv","zldb","zeg"])
def uegan(ydckd, frj):
    return ydckd[-2] == "ezdw" and frj[0] == "rcqr"
def osps(ydckd,frj):
    return not uegan(ydckd, frj)
mji = Factor("ckfq", [DerivedLevel("vbsggr", Window(uegan, [ydckd, frj],3,1)), DerivedLevel("qdpq", Window(osps, [ydckd, frj],3,1))])
### EXPERIMENT
design=[ydckd,frj,mji]
crossing=[mji]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END