from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_JrGsjQS_ac = Factor("5JrGsjQS0ac", ["$QmMKda", "uFqH~NdBPvw", "bPM", "zyM", "OIBgN"])
OMsoAsh_VrtU = Factor("OMsoAsh!VrtU", ["lq!Ez", "rqevcqq<N", "bxcdB", "x:a2WsaUMC>;Yj", "T?jq"])


design=[_JrGsjQS_ac,OMsoAsh_VrtU]
crossing=[_JrGsjQS_ac,OMsoAsh_VrtU]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_0"))

### END
