from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hruxe = Factor("hruxe", ["ejbn","vblag","ksrq","epttpg","uyp","mooj","zwqnb","yojs"])
whb = Factor("whb", ["bxz","wwmca","ixvf","wod","dzxlz","rwip","kmf","bpt"])
def zyi(hruxe, whb):
     return hruxe[-1] == "ejbn" and whb[0] != "ixvf"
def xkwzk(hruxe, whb):
     return hruxe[-1] != "ejbn" and whb[0] == "ixvf"
def jgutjj(hruxe, whb):
     return (not zyi(hruxe, whb)) and (whb[0] != "ixvf")
undztl = Factor("ftubtu", [DerivedLevel("mzyagu", Transition(zyi, [hruxe, whb])), DerivedLevel("mlgu", Transition(xkwzk, [hruxe, whb])),DerivedLevel("glezlm", Transition(jgutjj, [hruxe, whb]))])
### EXPERIMENT
design=[hruxe,whb,undztl]
crossing=[undztl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END