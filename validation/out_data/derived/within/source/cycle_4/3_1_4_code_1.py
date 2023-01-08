from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
txj = Factor("txj", ["qkuf","zbrskh","woqju","njhij","jjba","uotas","uzfvp"])
def gria(txj):
     return txj == "zbrskh"
def utw(txj):
     return txj == "woqju"
def bwsxmp(txj):
     return (txj != "zbrskh") and (txj != "woqju")
xxyxvk = Factor("brx", [DerivedLevel("logc", WithinTrial(gria, [txj])), DerivedLevel("lhavt", WithinTrial(utw, [txj])),DerivedLevel("wrcs", WithinTrial(bwsxmp, [txj]))])
### EXPERIMENT
design=[txj,xxyxvk]
crossing=[xxyxvk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END