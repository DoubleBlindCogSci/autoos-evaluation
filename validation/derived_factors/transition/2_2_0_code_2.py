from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oyjjvq = Factor("oyjjvq", ["izk","dok","kcnrhz","erpusv","lftdl","pal","ukmnw"])
pci = Factor("pci", ["bjs","nnwbkt","cvrzdw","pld","agium","mnb","kgyfy"])
def is_bib_dovw(oyjjvq, pci):
    return oyjjvq[0] != "lftdl" or pci[0] != "kgyfy"
def is_bib_gga(oyjjvq, pci):
    return not is_bib_dovw(oyjjvq, pci)
bib = Factor("bib", [DerivedLevel("dovw", Transition(is_bib_dovw, [oyjjvq, pci])), DerivedLevel("gga", Transition(is_bib_gga, [oyjjvq, pci]))])

design=[oyjjvq,pci,bib]
crossing=[bib]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END