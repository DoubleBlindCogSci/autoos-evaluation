from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ufyr= Factor("ufyr", ["bgcnrq","aoztp","lpne","wrrgn","ovlvx","zeedt","dipr"])
def is_itei_pmc(ufyr):
    return ufyr[0] == "dipr" and ufyr[-1] != "lpne"
def is_itei_ejm(ufyr):
    return not is_itei_pmc(ufyr)
itei= Factor("itei", [DerivedLevel("pmc", Window(is_itei_pmc, [ufyr], 3, 1)), DerivedLevel("ejm", Window(is_itei_ejm, [ufyr], 3, 1))])

design=[ufyr,itei]
crossing=[itei]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
