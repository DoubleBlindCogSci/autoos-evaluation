from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
K__YSnO = Factor("K4*YSnO", ["qh7HlEdQ>X^So", "rAPZ^pks2", ":tdvuIdM_NIeAo", "dXKX ", "pAr", "[8r", "lgulPGcnZt_tnS"])
W__pRbUvx = Factor("W<(pRbUvx", ["XX^vopHE", "!ki9ohJS@aI", "nMgiVw", "qWpxsjddz", "sbNz", "gKCBwAT", "wzXIIJx"])

design=[K__YSnO,W__pRbUvx]
crossing=[K__YSnO,W__pRbUvx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_2_0"))

### END
