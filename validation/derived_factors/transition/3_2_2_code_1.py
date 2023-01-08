from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mhlntl = Factor("mhlntl", ["bmkp","gyup","yzpve","ysj","gtxusf","nshkc"])
iqiac = Factor("iqiac", ["oiffr","yjfxkd","warzfy","uvjgcj","venv","rxz","rkbbpe","kkbhry"])
def ydenba(mhlntl, iqiac):
     return "bmkp" == mhlntl[-1] and iqiac[0] != "oiffr"
def nfqoag(mhlntl, iqiac):
     return "bmkp" != mhlntl[-1] and iqiac[0] == "oiffr"
def fbi(mhlntl, iqiac):
     return (not mhlntl[-1] == "bmkp") and (not iqiac[0] == "oiffr")
ealmpn = Factor("wua", [DerivedLevel("ifirm", Transition(ydenba, [mhlntl, iqiac])), DerivedLevel("kjv", Transition(nfqoag, [mhlntl, iqiac])),DerivedLevel("ydl", Transition(fbi, [mhlntl, iqiac]))])
### EXPERIMENT
design=[mhlntl,iqiac,ealmpn]
crossing=[ealmpn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END