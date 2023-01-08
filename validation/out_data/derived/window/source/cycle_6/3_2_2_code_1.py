from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mch = Factor("mch", ["qcorlu","iufm","uqj","vba","cid","wdpce"])
yno = Factor("yno", ["mfzqrp","sqaa","lgpdao","pkosa","oyid","wtitea","kzgaih"])
def fgdj(mch, yno):
     return "cid" == mch[-1] and not yno[-2] == "wtitea"
def qrevi(mch, yno):
     return "cid" != mch[-1] and  yno[-2] == "wtitea"
def jir(mch, yno):
     return (mch[-1] != "cid") and (not yno[-2] == "wtitea")
anel = Factor("rlxwtt", [DerivedLevel("yrk", Window(fgdj, [mch, yno],3,1)), DerivedLevel("uvv", Window(qrevi, [mch, yno],3,1)),DerivedLevel("hgdxmx", Window(jir, [mch, yno],3,1))])
### EXPERIMENT
design=[mch,yno,anel]
crossing=[anel]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END