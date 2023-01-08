from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ijpw = Factor("ijpw", ["iya","pjrywo","niuvji","cqy","mmcg"])
def khez(ijpw):
    return ijpw != "iya"
def xqvg(ijpw):
    return not (ijpw != "iya")
kpteav = DerivedLevel("jxot", WithinTrial(khez, [ijpw]))
krbvpn = DerivedLevel("khyach", WithinTrial(xqvg, [ijpw]))
qhc = Factor("cqzazp", [kpteav, krbvpn])

### EXPERIMENT
design=[ijpw,qhc]
crossing=[qhc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END