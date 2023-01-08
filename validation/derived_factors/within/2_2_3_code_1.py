from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
phnv = Factor("phnv", ["aiii","txybhd","yineo","cssbs","dbhsj"])
olzqq = Factor("olzqq", ["aiii","txybhd","yineo","cssbs","dbhsj"])
nrbb = Factor("nrbb", ["aiii","txybhd","yineo","cssbs","dbhsj"])
def mshdmf(phnv, olzqq, nrbb):
    return phnv == olzqq and phnv != nrbb
def utnov(phnv, olzqq, nrbb):
    return not (phnv == olzqq) or not (phnv != nrbb)
fmjmly = Factor("nbt", [DerivedLevel("cnhtvb", WithinTrial(mshdmf, [phnv, olzqq, nrbb])), DerivedLevel("fdaxx", WithinTrial(utnov, [phnv, olzqq, nrbb]))])
### EXPERIMENT
design=[phnv,olzqq,nrbb,fmjmly]
crossing=[fmjmly]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END