from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tlahu = Factor("tlahu", ["pgb","xzptv","juvf","kmsmbb","pvas","lbmeii"])
cmjg = Factor("cmjg", ["zxv","nppzc","spwnx","dxqe","uvaiu","cpdcp"])
def urtpsq(tlahu, cmjg):
     return "juvf" == tlahu
def shctx(tlahu, cmjg):
     return tlahu != "juvf" and  cmjg == "nppzc"
def qfeap(tlahu, cmjg):
     return (not tlahu == "juvf") and (cmjg != "nppzc")
qzzovl = Factor("zgmb", [DerivedLevel("punz", WithinTrial(urtpsq, [tlahu, cmjg])), DerivedLevel("ufp", WithinTrial(shctx, [tlahu, cmjg])),DerivedLevel("hzs", WithinTrial(qfeap, [tlahu, cmjg]))])
### EXPERIMENT
design=[tlahu,cmjg,qzzovl]
crossing=[qzzovl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END