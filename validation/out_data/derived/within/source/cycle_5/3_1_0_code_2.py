from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hbuxa = Factor("hbuxa", ["rjsas","oeqkkr","aqp","tume","brdk","kvrxxd","jcth","veokra"])
def is_uqz_hgreb(hbuxa):
    return hbuxa == "brdk"
def is_uqz_jrq(hbuxa):
    return hbuxa == "tume"
def is_uqz_oqkw(hbuxa):
    return not (is_uqz_hgreb(hbuxa) or is_uqz_jrq(hbuxa))
uqz = Factor("uqz", [DerivedLevel("hgreb", WithinTrial(is_uqz_hgreb, [hbuxa])), DerivedLevel("jrq", WithinTrial(is_uqz_jrq, [hbuxa])), DerivedLevel("oqkw", WithinTrial(is_uqz_oqkw, [hbuxa]))])

design=[hbuxa,uqz]
crossing=[uqz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END