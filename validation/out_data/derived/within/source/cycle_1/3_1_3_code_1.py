from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jqghz = Factor("jqghz", ["cladjy","haqvq","wersx","aqyi","bdds","jtzc","apqtow","axu"])
def veub(jqghz):
     return "bdds" == jqghz
def xnq(jqghz):
     return "jtzc" == jqghz
def tsbh(jqghz):
     return (not veub(jqghz)) and (not jqghz == "jtzc")
vpto = Factor("kctzbv", [DerivedLevel("yvvzxe", WithinTrial(veub, [jqghz])), DerivedLevel("ymvhv", WithinTrial(xnq, [jqghz])),DerivedLevel("kci", WithinTrial(tsbh, [jqghz]))])
### EXPERIMENT
design=[jqghz,vpto]
crossing=[vpto]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END