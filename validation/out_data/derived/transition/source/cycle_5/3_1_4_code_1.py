from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kcjg = Factor("kcjg", ["xal","yxlmog","nepg","nft","wdnjd","wzx","ltwgre","bbj"])
def ejzc(kcjg):
     return kcjg[0] == "wzx" and kcjg[-1] != "nft"
def snzycc(kcjg):
     return (not "wzx" != kcjg[0]) and  kcjg[-1] == "nft"
def wve(kcjg):
     return (kcjg[0] != "wzx") and (kcjg[-1] != "nft")
mhrlqc = Factor("fpzy", [DerivedLevel("ivdsvt", Transition(ejzc, [kcjg])), DerivedLevel("ngq", Transition(snzycc, [kcjg])),DerivedLevel("enjasj", Transition(wve, [kcjg]))])
### EXPERIMENT
design=[kcjg,mhrlqc]
crossing=[mhrlqc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END