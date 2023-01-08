from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
duxbo= Factor("duxbo", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
cbrnt= Factor("cbrnt", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
rep= Factor("rep", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
def is_nxqa_xbata(cbrnt, duxbo):
    return cbrnt[0] == duxbo[-1]
def is_nxqa_qzxb(cbrnt, duxbo, rep):
    return cbrnt[0] != duxbo[-1] and rep[0] == duxbo[-1]
def is_nxqa_bfl(cbrnt, duxbo, rep):
    return not (is_nxqa_xbata(cbrnt, duxbo) or is_nxqa_qzxb(cbrnt, duxbo, rep))
nxqa= Factor("nxqa", [DerivedLevel("xbata", Transition(is_nxqa_xbata, [cbrnt, duxbo])), DerivedLevel("qzxb", Transition(is_nxqa_qzxb, [cbrnt, duxbo, rep])), DerivedLevel("bfl", Transition(is_nxqa_bfl, [cbrnt, duxbo, rep]))])

design=[duxbo,cbrnt,rep,nxqa]
crossing=[nxqa]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
