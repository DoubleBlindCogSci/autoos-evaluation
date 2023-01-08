from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
duxbo = Factor("duxbo", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
cbrnt = Factor("cbrnt", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
rep = Factor("rep", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
def orgfgw(duxbo, cbrnt, rep):
     return cbrnt[-1] == duxbo[0]
def iqjn(duxbo, cbrnt, rep):
     return cbrnt[-1] != duxbo[0] and rep[0] == duxbo[-1]
def llt(duxbo, cbrnt, rep):
     return (not duxbo[0] == cbrnt[-1]) and (not iqjn(duxbo, cbrnt, rep))
ubfyl = Factor("nxqa", [DerivedLevel("xbata", Transition(orgfgw, [duxbo, cbrnt, rep])), DerivedLevel("qzxb", Transition(iqjn, [duxbo, cbrnt, rep])),DerivedLevel("bfl", Transition(llt, [duxbo, cbrnt, rep]))])
### EXPERIMENT
design=[duxbo,cbrnt,rep,ubfyl]
crossing=[ubfyl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END