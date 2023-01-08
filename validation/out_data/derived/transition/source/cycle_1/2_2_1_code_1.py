from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ufgywf = Factor("ufgywf", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
rudnb = Factor("rudnb", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
inb = Factor("inb", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
def jfskg(ufgywf, rudnb, inb):
    return ufgywf[0] == rudnb[-1]
def ncwv(ufgywf, rudnb, inb):
    return ufgywf[0] != rudnb[-1]
cqzpz = Factor("jxoudi", [DerivedLevel("epi", Transition(jfskg, [ufgywf, rudnb, inb])), DerivedLevel("oeefb", Transition(ncwv, [ufgywf, rudnb, inb]))])
### EXPERIMENT
design=[ufgywf,rudnb,inb,cqzpz]
crossing=[cqzpz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END