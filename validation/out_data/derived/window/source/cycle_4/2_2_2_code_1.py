from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
molokf = Factor("molokf", ["zihb","ffmhv","pyklyv","etbiy","xhrx"])
ooyt = Factor("ooyt", ["hlhdjb","hhd","vaq","rdv","hoin","qte","opv"])
def jtgqu(molokf, ooyt):
    return molokf[-3] == "zihb" and ooyt[-2] != "hoin"
def hzbbg(molokf,ooyt):
    return molokf[-3] != "zihb" or not (ooyt[-2] != "hoin")
pahzol = Factor("mod", [DerivedLevel("lgdc", Window(jtgqu, [molokf, ooyt],4,1)), DerivedLevel("pmkjr", Window(hzbbg, [molokf, ooyt],4,1))])
### EXPERIMENT
design=[molokf,ooyt,pahzol]
crossing=[pahzol]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END