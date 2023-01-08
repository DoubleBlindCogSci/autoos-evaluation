from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wmfo = Factor("wmfo", ["pdloah", "kgpj"])
rqhpgd = Factor("rqhpgd", ["tzflh", "mqlae"])
jobz = Factor("jobz", ["qeweeh", "uxvd"])
ygd = Factor("ygd", ["vll", "yhhwqb"])
tbfb = Factor("tbfb", ["jgjwtk", "rnmpmf"])
aik = Factor("aik", ["sbzmfr", "pqpwy"])

### EXPERIMENT
design=[wmfo,rqhpgd,jobz,ygd,tbfb,aik]
crossing=[[wmfo,rqhpgd,jobz,ygd,tbfb,aik]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_7"))
### END