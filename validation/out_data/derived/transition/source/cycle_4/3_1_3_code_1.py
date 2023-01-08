from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kgtk = Factor("kgtk", ["rgved","ukpjpb","sfyyo","wcf","jitg","dmwzq","vnuph"])
def znkva(kgtk):
     return kgtk[0] == "sfyyo" and kgtk[-1] != "rgved"
def nwadb(kgtk):
     return (not "sfyyo" != kgtk[0]) and  "rgved" == kgtk[-1]
def xpozgg(kgtk):
     return (kgtk[0] != "sfyyo") and (not kgtk[-1] == "rgved")
ufa = Factor("gkzn", [DerivedLevel("pyxd", Transition(znkva, [kgtk])), DerivedLevel("dlyye", Transition(nwadb, [kgtk])),DerivedLevel("yydfj", Transition(xpozgg, [kgtk]))])
### EXPERIMENT
design=[kgtk,ufa]
crossing=[ufa]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END