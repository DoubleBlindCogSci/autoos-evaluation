from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ljq = Factor("ljq", ["wwc", "etqof"])
kuqcw = Factor("kuqcw", ["ygrywf", "xlr"])
ied = Factor("ied", ["ttay", "grjpd"])
zcvtxv = Factor("zcvtxv", ["ixaef", "llve"])
agaa = Factor("agaa", ["sqsyas", "fxwm"])
fftli = Factor("fftli", ["twfy", "vtpn"])
constraints = []
crossing = [[ljq, kuqcw, ied], [zcvtxv, agaa, fftli]]


design=[ljq,kuqcw,ied,zcvtxv,agaa,fftli]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_4"))

### END