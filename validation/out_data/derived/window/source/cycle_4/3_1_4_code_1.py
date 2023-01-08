from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
miyzdq = Factor("miyzdq", ["klaaay","qyw","vmzbe","jzywnf","kklavl","aalk","zyek","dtpi"])
def kcmci(miyzdq):
     return miyzdq[-2] == "klaaay" and not miyzdq[0] == "klaaay"
def senihx(miyzdq):
     return not "klaaay" == miyzdq[-2] and  miyzdq[0] == "aalk"
def poxpf(miyzdq):
     return (not miyzdq[-2] == "klaaay") and (not miyzdq[0] == "aalk")
vqvtj = Factor("brsv", [DerivedLevel("animf", Window(kcmci, [miyzdq],3,1)), DerivedLevel("dpmihp", Window(senihx, [miyzdq],3,1)),DerivedLevel("ypsd", Window(poxpf, [miyzdq],3,1))])
### EXPERIMENT
design=[miyzdq,vqvtj]
crossing=[vqvtj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END