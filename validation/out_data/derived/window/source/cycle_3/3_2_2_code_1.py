from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
inm = Factor("inm", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
qcbti = Factor("qcbti", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
rmwf = Factor("rmwf", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
def tdiun(inm, rmwf, qcbti):
     return rmwf[-1] == inm[0] and inm[-1] != qcbti[0]
def zxxyds(inm, rmwf, qcbti):
     return rmwf[-1] != inm[0] and qcbti[0] == inm[-1]
def eci(inm, rmwf, qcbti):
     return (not tdiun(inm, rmwf, qcbti)) and (inm[-1] != qcbti[0])
mozvr = DerivedLevel("ovxpz", Window(tdiun, [inm, qcbti, rmwf],2,1))
dazbpb = DerivedLevel("ojx", Window(zxxyds, [inm, qcbti, rmwf],2,1))
vbgfp = DerivedLevel("akwq", Window(eci, [inm, qcbti, rmwf],2,1))
ujsl = Factor("reyloi", [mozvr, dazbpb, vbgfp])

### EXPERIMENT
design=[inm,qcbti,rmwf,ujsl]
crossing=[ujsl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END