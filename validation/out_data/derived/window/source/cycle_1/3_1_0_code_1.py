from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vxqndv = Factor("vxqndv", ["egnpd","aof","ybec","jcamd","gocgh","qcdyxn"])
def fnr(vxqndv):
     return vxqndv[-2] == "jcamd"
def wbfb(vxqndv):
     return "egnpd" == vxqndv[0]
def ayno(vxqndv):
     return (vxqndv[-2] != "jcamd") and (not wbfb(vxqndv))
innvkv = Factor("tyruji", [DerivedLevel("kbpq", Window(fnr, [vxqndv],3,1)), DerivedLevel("bmb", Window(wbfb, [vxqndv],3,1)),DerivedLevel("nfzkw", Window(ayno, [vxqndv],3,1))])
### EXPERIMENT
design=[vxqndv,innvkv]
crossing=[innvkv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END