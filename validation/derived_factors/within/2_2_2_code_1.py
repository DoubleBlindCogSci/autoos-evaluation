from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ymx = Factor("ymx", ["umrac","oiyp","doh","gffs","xsxf","vrq","ebsuz"])
faaj = Factor("faaj", ["oxoita","stagx","fsjrz","yxsrm","gbt","ympq"])
def aewv(ymx, faaj):
    return ymx != "gffs" or faaj == "stagx"
def ytqoce(ymx,faaj):
    return not aewv(ymx, faaj)
daki = DerivedLevel("pcrjo", WithinTrial(aewv, [ymx, faaj]))
rxsq = DerivedLevel("hdfn", WithinTrial(ytqoce, [ymx, faaj]))
lgusa = Factor("orez", [daki, rxsq])

### EXPERIMENT
design=[ymx,faaj,lgusa]
crossing=[lgusa]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END