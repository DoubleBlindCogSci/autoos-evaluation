from sweetpea import *
import os
_dir=os.path.dirname(__file__)
tqsng = Factor("tqsng", ["bhda", "akda"])
mkh = Factor("mkh", ["takc", "gutyuz"])
fieq = Factor("fieq", ["blelt", "cbb"])
fljmr = Factor("fljmr", ["bvwupc", "iwlcuk"])
ktpjut = Factor("ktpjut", ["shteo", "dsgk"])
constraints = []
crossing = [tqsng, mkh, fieq, fljmr, ktpjut]


design=[tqsng,mkh,fieq,fljmr,ktpjut]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_4"))

### END