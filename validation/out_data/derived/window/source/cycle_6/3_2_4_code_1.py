from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ffw = Factor("ffw", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
qce = Factor("qce", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
atrss = Factor("atrss", ["zjewp","mfde","tsg","vjqa","yrskd","omo","xfkz"])
def lgdsy(ffw, qce, atrss):
     return ffw[0] == qce[-2] and ffw[-2] != atrss[0]
def ejngje(ffw, qce, atrss):
     return qce[-2] != ffw[0] and atrss[0] == ffw[-2]
def olufed(ffw, qce, atrss):
     return (not lgdsy(ffw, qce, atrss)) and (not ejngje(ffw, qce, atrss))
rprlew = Factor("sscn", [DerivedLevel("yrewqx", Window(lgdsy, [ffw, qce, atrss],3,1)), DerivedLevel("qsx", Window(ejngje, [ffw, qce, atrss],3,1)),DerivedLevel("uoskx", Window(olufed, [ffw, qce, atrss],3,1))])
### EXPERIMENT
design=[ffw,qce,atrss,rprlew]
crossing=[rprlew]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END