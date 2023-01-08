from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vzweak = Factor("vzweak", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
dsrncz = Factor("dsrncz", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
nwdg = Factor("nwdg", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
def wcmpva(vzweak, dsrncz, nwdg):
     return dsrncz[-1] == vzweak[0] and vzweak[-1] != nwdg[0]
def qgrfup(vzweak, dsrncz, nwdg):
     return dsrncz[-1] != vzweak[0] and vzweak[-1] == nwdg[0]
def dlqf(vzweak, dsrncz, nwdg):
     return (not vzweak[0] == dsrncz[-1]) and (not vzweak[-1] == nwdg[0])
pkptrb = Factor("cij", [DerivedLevel("gkutnp", Transition(wcmpva, [vzweak, dsrncz, nwdg])), DerivedLevel("qpmdhc", Transition(qgrfup, [vzweak, dsrncz, nwdg])),DerivedLevel("ezj", Transition(dlqf, [vzweak, dsrncz, nwdg]))])
### EXPERIMENT
design=[vzweak,dsrncz,nwdg,pkptrb]
crossing=[pkptrb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END