from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
guh = Factor("guh", ["icgxd","rio","nfnij","spbm","jtmifq","bzfnd"])
def wcazr(guh):
     return "rio" == guh
def uwix(guh):
     return "nfnij" == guh
def ppkhmi(guh):
     return (not wcazr(guh)) and (not guh == "nfnij")
cqv = DerivedLevel("rdl", WithinTrial(wcazr, [guh]))
bybm = DerivedLevel("grs", WithinTrial(uwix, [guh]))
tfopm = DerivedLevel("vujbce", WithinTrial(ppkhmi, [guh]))
pptqih = Factor("jobcfs", [cqv, bybm, tfopm])

### EXPERIMENT
design=[guh,pptqih]
crossing=[pptqih]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END