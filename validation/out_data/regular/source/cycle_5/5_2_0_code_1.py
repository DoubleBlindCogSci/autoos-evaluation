from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OA3zy7i84R8=Factor("5JrGsjQS0ac",['$QmMKda',"uFqH~NdBPvw","bPM",'zyM','OIBgN'])
YtyK12=Factor("OMsoAsh!VrtU",["lq!Ez",'rqevcqq<N',"bxcdB","x:a2WsaUMC>;Yj","T?jq"])

### EXPERIMENT
design=[OA3zy7i84R8,YtyK12]
crossing=[OA3zy7i84R8,YtyK12]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_0"))
### END