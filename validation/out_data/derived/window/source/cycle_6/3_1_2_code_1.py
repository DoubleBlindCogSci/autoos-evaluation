from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ptqz = Factor("ptqz", ["ris","hkeewa","htq","hqizy","zya","qudqay","bigo","ftgj"])
def ayaavv(ptqz):
     return "hqizy" == ptqz[0] and not ptqz[-1] == "hqizy"
def pjb(ptqz):
     return not "hqizy" == ptqz[0] and  ptqz[-1] == "qudqay"
def yetd(ptqz):
     return (not ptqz[0] == "hqizy") and (not pjb(ptqz))
sbd = Factor("vge", [DerivedLevel("dkhvb", Window(ayaavv, [ptqz],2,1)), DerivedLevel("xhb", Window(pjb, [ptqz],2,1)),DerivedLevel("wvdtqo", Window(yetd, [ptqz],2,1))])
### EXPERIMENT
design=[ptqz,sbd]
crossing=[sbd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END