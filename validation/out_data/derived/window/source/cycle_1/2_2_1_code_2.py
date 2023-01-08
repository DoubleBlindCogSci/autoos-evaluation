from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rrinkq= Factor("rrinkq", ["nygyo","ejtynj","lfsjhb","tdxd","qui","eroovc"])
nrt= Factor("nrt", ["qwwz","tmmwnj","xbyya","pxg","ybe","muwdn","xce"])

def is_bsgkzr_bzafu(rrinkq, nrt):
    return rrinkq[0] != "ejtynj" or nrt[0] == "pxg"
def is_bsgkzr_doedz(rrinkq, nrt):
    return rrinkq[0] == "ejtynj" and nrt[0] != "pxg"
bsgkzr= Factor("bsgkzr", [DerivedLevel("bzafu", Window(is_bsgkzr_bzafu, [rrinkq, nrt], 4, 1)), DerivedLevel("doedz", Window(is_bsgkzr_doedz, [rrinkq, nrt], 4, 1))])


design=[rrinkq,nrt,bsgkzr]
crossing=[bsgkzr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
