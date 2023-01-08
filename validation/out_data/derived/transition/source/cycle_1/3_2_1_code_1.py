from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pbdufo = Factor("pbdufo", ["vpd","avmt","fkdx","bvs","ukkqbx","trbcm","ygizr","vgdy"])
bij = Factor("bij", ["ibqt","gvvyt","ssvls","dpwx","mui","bwsmwk","jid","jdxfe"])
def soc(pbdufo, bij):
     return "bvs" == pbdufo[-1]
def mzfxbp(pbdufo, bij):
     return "bvs" != pbdufo[-1] and  bij[0] == "ssvls"
def mme(pbdufo, bij):
     return (pbdufo[-1] != "bvs") and (not bij[0] == "ssvls")
tdrvi = Factor("rew", [DerivedLevel("cjl", Transition(soc, [pbdufo, bij])), DerivedLevel("zfzme", Transition(mzfxbp, [pbdufo, bij])),DerivedLevel("ipcih", Transition(mme, [pbdufo, bij]))])
### EXPERIMENT
design=[pbdufo,bij,tdrvi]
crossing=[tdrvi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END