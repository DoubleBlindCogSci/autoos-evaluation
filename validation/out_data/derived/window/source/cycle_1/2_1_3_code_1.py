from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ufyr = Factor("ufyr", ["bgcnrq","aoztp","lpne","wrrgn","ovlvx","zeedt","dipr"])
def obft(ufyr):
    return ufyr[-2] == "dipr" and ufyr[0] != "lpne"
def yse(ufyr):
    return ufyr[-2] != "dipr" or ufyr[0] == "lpne"
gsl = DerivedLevel("pmc", Window(obft, [ufyr],3,1))
fofi = DerivedLevel("ejm", Window(yse, [ufyr],3,1))
kvyy = Factor("itei", [gsl, fofi])

### EXPERIMENT
design=[ufyr,kvyy]
crossing=[kvyy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END