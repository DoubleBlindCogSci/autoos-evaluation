from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rwkex = Factor("rwkex", ["ievjo","oaostz","uxhbc","hlyauw","lis","otcr"])
def jheukf(rwkex):
     return "hlyauw" == rwkex[0] and not rwkex[-1] == "lis"
def qgsbvq(rwkex):
     return (not "hlyauw" != rwkex[0]) and  "lis" == rwkex[-1]
def utl(rwkex):
     return (not rwkex[0] == "hlyauw") and (not rwkex[-1] == "lis")
ouxtg = DerivedLevel("ufpf", Transition(jheukf, [rwkex]))
hgnj = DerivedLevel("lrbn", Transition(qgsbvq, [rwkex]))
hep = DerivedLevel("mwop", Transition(utl, [rwkex]))
oqszcj = Factor("klc", [ouxtg, hgnj, hep])

### EXPERIMENT
design=[rwkex,oqszcj]
crossing=[oqszcj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END