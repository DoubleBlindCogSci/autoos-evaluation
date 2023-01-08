from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hbuxa = Factor("hbuxa", ["rjsas","oeqkkr","aqp","tume","brdk","kvrxxd","jcth","veokra"])
def ept(hbuxa):
     return hbuxa == "brdk"
def ujnn(hbuxa):
     return hbuxa == "tume"
def eus(hbuxa):
     return (not ept(hbuxa)) and (not ujnn(hbuxa))
bzeunw = DerivedLevel("hgreb", WithinTrial(ept, [hbuxa]))
uemh = DerivedLevel("jrq", WithinTrial(ujnn, [hbuxa]))
cmt = DerivedLevel("oqkw", WithinTrial(eus, [hbuxa]))
haacm = Factor("uqz", [bzeunw, uemh, cmt])

### EXPERIMENT
design=[hbuxa,haacm]
crossing=[haacm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END