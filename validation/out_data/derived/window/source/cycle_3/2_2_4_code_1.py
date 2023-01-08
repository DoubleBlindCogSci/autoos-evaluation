from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jzn = Factor("jzn", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
ehon = Factor("ehon", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
xtzkge = Factor("xtzkge", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
def pwe(jzn, xtzkge, ehon):
    return jzn[-2] == xtzkge[0] and jzn[0] != ehon[-2]
def ffs(jzn, xtzkge, ehon):
    return not pwe(jzn, xtzkge, ehon)
lqfvx = Factor("kultts", [DerivedLevel("wrn", Window(pwe, [jzn, ehon, xtzkge],3,1)), DerivedLevel("yrit", Window(ffs, [jzn, ehon, xtzkge],3,1))])
### EXPERIMENT
design=[jzn,ehon,xtzkge,lqfvx]
crossing=[lqfvx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END