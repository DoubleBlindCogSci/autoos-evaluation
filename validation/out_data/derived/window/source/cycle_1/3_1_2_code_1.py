from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rbem = Factor("rbem", ["zerp","pqyoqq","uzz","znwo","fzahge","uukrt","oqiqce"])
def yiyqp(rbem):
     return "znwo" == rbem[-1]
def tzd(rbem):
     return rbem[-3] == "pqyoqq"
def nrf(rbem):
     return (not yiyqp(rbem)) and (not rbem[-3] == "pqyoqq")
hhw = Factor("efpet", [DerivedLevel("bzh", Window(yiyqp, [rbem],4,1)), DerivedLevel("edv", Window(tzd, [rbem],4,1)),DerivedLevel("ymqe", Window(nrf, [rbem],4,1))])
### EXPERIMENT
design=[rbem,hhw]
crossing=[hhw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END