from sweetpea import *
import os
_dir=os.path.dirname(__file__)
wmfo = Factor("wmfo", ["pdloah", "kgpj"])
rqhpgd = Factor("rqhpgd", ["tzflh", "mqlae"])
jobz = Factor("jobz", ["qeweeh", "uxvd"])
ygd = Factor("ygd", ["vll", "yhhwqb"])
tbfb = Factor("tbfb", ["jgjwtk", "rnmpmf"])
aik = Factor("aik", ["sbzmfr", "pqpwy"])
constraints = []
crossing = [wmfo, rqhpgd, jobz, ygd, tbfb, aik]


design=[wmfo,rqhpgd,jobz,ygd,tbfb,aik]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_7"))

### END