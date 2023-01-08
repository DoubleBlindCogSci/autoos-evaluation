from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_bRxu_nA_A= Factor("]bRxu?nA!A", [Level("yh#SkZ$I", 1), Level("Y%ou~IceHMu:Br", 8), Level("SeBL", 1), Level("l}gPXP0i", 1)])
BBK_lP_nOHZ_Y= Factor("BBK]lP@nOHZ@Y", [Level("FcPaPVVD;BuOtQ", 1), Level("(nweqHF(hl", 1), Level("GMJiBe", 9), Level("wI7n6filLu", 1)])

design=[_bRxu_nA_A,BBK_lP_nOHZ_Y]
crossing=[_bRxu_nA_A,BBK_lP_nOHZ_Y]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_2_0"))

### END
