from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kekvlw = Factor("kekvlw", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
fpcf = Factor("fpcf", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
cbbiqs = Factor("cbbiqs", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
def bzlngb(kekvlw, cbbiqs, fpcf):
     return cbbiqs[-1] == kekvlw[0]
def hrh(kekvlw, cbbiqs, fpcf):
     return cbbiqs[-1] != kekvlw[0] and fpcf[0] == kekvlw[-1]
def chofh(kekvlw, cbbiqs, fpcf):
     return (not kekvlw[0] == cbbiqs[-1]) and (not kekvlw[-1] == fpcf[0])
ozflzc = DerivedLevel("iwbpyw", Transition(bzlngb, [kekvlw, fpcf, cbbiqs]))
lmbz = DerivedLevel("drcljo", Transition(hrh, [kekvlw, fpcf, cbbiqs]))
xjeuuy = DerivedLevel("jxgp", Transition(chofh, [kekvlw, fpcf, cbbiqs]))
gzqze = Factor("fjl", [ozflzc, lmbz, xjeuuy])

### EXPERIMENT
design=[kekvlw,fpcf,cbbiqs,gzqze]
crossing=[gzqze]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END