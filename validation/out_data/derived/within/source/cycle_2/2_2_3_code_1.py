from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ihlv = Factor("ihlv", ["dfuu","aramdr","yadl","vekpr","vvhj"])
ngheks = Factor("ngheks", ["sctvll","qjpsrm","anz","zsmnya","ifcx","xbcj","ganxoa"])
def oyf(ihlv, ngheks):
    return ihlv == "yadl" and ngheks == "ganxoa"
def kdv(ihlv,ngheks):
    return not (ihlv == "yadl") or ngheks != "ganxoa"
csxav = Factor("yxyzr", [DerivedLevel("psyro", WithinTrial(oyf, [ihlv, ngheks])), DerivedLevel("igmf", WithinTrial(kdv, [ihlv, ngheks]))])
### EXPERIMENT
design=[ihlv,ngheks,csxav]
crossing=[csxav]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END