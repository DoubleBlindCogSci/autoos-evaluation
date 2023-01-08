from sweetpea import *
import os
_dir=os.path.dirname(__file__)
lgbhcs = Factor("lgbhcs", ["nzay", "wmdht"])
nrkkwb = Factor("nrkkwb", ["ztwt", "iiveky"])
vcbfq = Factor("vcbfq", ["slvm", "yfagun"])
oue = Factor("oue", ["fmjdi", "bzb"])
pyihft = Factor("pyihft", ["hut", "zeqwkp"])
qng = Factor("qng", ["jtcr", "jjharn"])
hmf = Factor("hmf", ["ipx", "oiiltz"])
ozwkx = Factor("ozwkx", ["jvzx", "qmukn"])
constraints = []
crossing = [[lgbhcs, nrkkwb], [vcbfq, oue, pyihft, qng, hmf, ozwkx]]


design=[lgbhcs,nrkkwb,vcbfq,oue,pyihft,qng,hmf,ozwkx]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3"))

### END