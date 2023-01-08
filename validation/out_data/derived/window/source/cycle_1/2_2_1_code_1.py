from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rrinkq = Factor("rrinkq", ["nygyo","ejtynj","lfsjhb","tdxd","qui","eroovc"])
nrt = Factor("nrt", ["qwwz","tmmwnj","xbyya","pxg","ybe","muwdn","xce"])
def vsmx(rrinkq, nrt):
    return rrinkq[-2] != "ejtynj" or nrt[-3] == "pxg"
def nyfdt(rrinkq,nrt):
    return rrinkq[-2] == "ejtynj" and not (nrt[-3] == "pxg")
ihzeo = Factor("bsgkzr", [DerivedLevel("bzafu", Window(vsmx, [rrinkq, nrt],4,1)), DerivedLevel("doedz", Window(nyfdt, [rrinkq, nrt],4,1))])
### EXPERIMENT
design=[rrinkq,nrt,ihzeo]
crossing=[ihzeo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END