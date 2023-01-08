from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
oimbuy = Factor("oimbuy", ["zanj","byz","tcu","yhvjmi","eqmrf","aga","sykg"])
hppah = Factor("hppah", ["fiviro","eump","wmggtq","ewhvwh","glfbm","yvuvce","lsgw","skrxzy"])
def jewh(oimbuy, hppah):
     return "sykg" == oimbuy[-1] and hppah[0] != "eump"
def ctwjm(oimbuy, hppah):
     return "sykg" != oimbuy[-1] and hppah[0] == "eump"
def jxhntn(oimbuy, hppah):
     return (not oimbuy[-1] == "sykg") and (not ctwjm(oimbuy, hppah))
ppicq = Factor("pklwju", [DerivedLevel("pspk", Transition(jewh, [oimbuy, hppah])), DerivedLevel("gelwv", Transition(ctwjm, [oimbuy, hppah])),DerivedLevel("sswak", Transition(jxhntn, [oimbuy, hppah]))])
### EXPERIMENT
design=[oimbuy,hppah,ppicq]
crossing=[ppicq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END