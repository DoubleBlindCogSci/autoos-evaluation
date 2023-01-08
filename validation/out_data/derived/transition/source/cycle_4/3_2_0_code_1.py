from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jmz = Factor("jmz", ["jihy","vml","ualooh","zwib","okr","ltap"])
sqg = Factor("sqg", ["bxsq","cunuta","nxlob","vmuyd","ysq","xtn"])
def ves(jmz, sqg):
     return jmz[-1] == "jihy" and sqg[0] != "xtn"
def hzoqtd(jmz, sqg):
     return jmz[-1] != "jihy" and sqg[0] == "xtn"
def tjcetz(jmz, sqg):
     return (not jmz[-1] == "jihy") and (not sqg[0] == "xtn")
eiojv = Factor("zbhiv", [DerivedLevel("puhii", Transition(ves, [jmz, sqg])), DerivedLevel("wdcu", Transition(hzoqtd, [jmz, sqg])),DerivedLevel("kwuqg", Transition(tjcetz, [jmz, sqg]))])
### EXPERIMENT
design=[jmz,sqg,eiojv]
crossing=[eiojv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END