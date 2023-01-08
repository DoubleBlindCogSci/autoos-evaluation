from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sfjmyp = Factor("sfjmyp", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
upld = Factor("upld", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
wroo = Factor("wroo", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
def is_qykga_kkgk(sfjmyp, upld, wroo):
    return sfjmyp[0] == wroo[-2] and sfjmyp[-2] != upld[0]
def is_qykga_jpv(sfjmyp, upld, wroo):
    return wroo[-2] != sfjmyp[0] and sfjmyp[-2] == upld[0]
def is_qykga_wzrc(sfjmyp, upld, wroo):
    return not (is_qykga_kkgk(sfjmyp, upld, wroo) or is_qykga_jpv(sfjmyp, upld, wroo))
qykga= Factor("qykga", [DerivedLevel("kkgk", Window(is_qykga_kkgk, [sfjmyp, upld, wroo], 3, 1)), DerivedLevel("jpv", Window(is_qykga_jpv, [sfjmyp, upld, wroo], 3, 1)), DerivedLevel("wzrc", Window(is_qykga_wzrc, [sfjmyp, upld, wroo], 3, 1))])

design=[sfjmyp,upld,wroo,qykga]
crossing=[qykga]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
