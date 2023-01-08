from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pcg = Factor("pcg", ["dqrn","thzjgv","ptwa","anf","dglo","qsd","nto","eczl"])
def eta(pcg):
     return "dqrn" == pcg
def fkzxvj(pcg):
     return "eczl" == pcg
def eielo(pcg):
     return (pcg != "dqrn") and (not fkzxvj(pcg))
ubhk = Factor("fopjp", [DerivedLevel("ibta", WithinTrial(eta, [pcg])), DerivedLevel("bwkw", WithinTrial(fkzxvj, [pcg])),DerivedLevel("lsi", WithinTrial(eielo, [pcg]))])
### EXPERIMENT
design=[pcg,ubhk]
crossing=[ubhk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END