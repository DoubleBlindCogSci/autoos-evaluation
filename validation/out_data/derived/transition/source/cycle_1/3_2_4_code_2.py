from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kekvlw= Factor("kekvlw", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
fpcf= Factor("fpcf", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
cbbiqs= Factor("cbbiqs", ["znvr","gdmc","hkozq","rxu","bzrshc","eksbhu"])
def is_fjl_iwbpyw(cbbiqs, kekvlw):
    return cbbiqs[0] == kekvlw[-1]
def is_fjl_drcljo(cbbiqs, kekvlw, fpcf):
    return cbbiqs[0] != kekvlw[-1] and fpcf[0] == kekvlw[-1]
def is_fjl_jxgp(cbbiqs, kekvlw, fpcf):
    return not (is_fjl_iwbpyw(cbbiqs, kekvlw) or is_fjl_drcljo(cbbiqs, kekvlw, fpcf))
fjl= Factor("fjl", [DerivedLevel("iwbpyw", Transition(is_fjl_iwbpyw, [cbbiqs, kekvlw])), DerivedLevel("drcljo", Transition(is_fjl_drcljo, [cbbiqs, kekvlw, fpcf])), DerivedLevel("jxgp", Transition(is_fjl_jxgp, [cbbiqs, kekvlw, fpcf]))])

design=[kekvlw,fpcf,cbbiqs,fjl]
crossing=[fjl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
