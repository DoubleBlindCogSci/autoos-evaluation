from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
igge = Factor("igge", ["tyd","nmmpt","dyzqcq","xkwqu","rzwhpo","grrdhv"])
xsbior = Factor("xsbior", ["dke","rfmr","vbwyr","pqp","awnmbl","wrl"])
def ddiyy(igge, xsbior):
    return igge[-1] != "xkwqu" or xsbior[0] != "wrl"
def aimnb(igge,xsbior):
    return igge[-1] == "xkwqu" and xsbior[0] == "wrl"
xttu = Factor("fofjlr", [DerivedLevel("oiuoqk", Window(ddiyy, [igge, xsbior],2,1)), DerivedLevel("alnlm", Window(aimnb, [igge, xsbior],2,1))])
### EXPERIMENT
design=[igge,xsbior,xttu]
crossing=[xttu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END