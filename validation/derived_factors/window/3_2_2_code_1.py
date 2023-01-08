from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iwp = Factor("iwp", ["jpx","ldmbjp","nyocl","eez","nxwmx","xkdgn"])
hbo = Factor("hbo", ["qyqzgn","mdk","eep","kerur","duc","bbidzv"])
def cgtvge(iwp, hbo):
     return iwp[-2] == "xkdgn" and hbo[-1] != "qyqzgn"
def qhlyvw(iwp, hbo):
     return "xkdgn" != iwp[-2] and  hbo[-1] == "qyqzgn"
def jdj(iwp, hbo):
     return (iwp[-2] != "xkdgn") and (not qhlyvw(iwp, hbo))
wqc = Factor("wfq", [DerivedLevel("wcu", Window(cgtvge, [iwp, hbo],3,1)), DerivedLevel("dbxyui", Window(qhlyvw, [iwp, hbo],3,1)),DerivedLevel("wwtvi", Window(jdj, [iwp, hbo],3,1))])
### EXPERIMENT
design=[iwp,hbo,wqc]
crossing=[wqc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END