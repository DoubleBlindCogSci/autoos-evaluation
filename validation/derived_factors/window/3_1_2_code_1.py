from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kwkk = Factor("kwkk", ["mcsefi","fhnn","jpyv","ayyi","gbg","jdj"])
def iqofzy(kwkk):
     return "gbg" == kwkk[-1] and not kwkk[0] == "gbg"
def wbhcm(kwkk):
     return not "gbg" == kwkk[-1] and  kwkk[0] == "jpyv"
def qavbns(kwkk):
     return (not iqofzy(kwkk)) and (kwkk[0] != "jpyv")
mgapxw = Factor("rdr", [DerivedLevel("mietsj", Window(iqofzy, [kwkk],2,1)), DerivedLevel("bevmb", Window(wbhcm, [kwkk],2,1)),DerivedLevel("mtl", Window(qavbns, [kwkk],2,1))])
### EXPERIMENT
design=[kwkk,mgapxw]
crossing=[mgapxw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END