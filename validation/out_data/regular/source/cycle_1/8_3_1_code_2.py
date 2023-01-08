from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OKJR_bFabtyQS= Factor("OKJR!bFabtyQS", [Level("qCi~_UREBIb", 1), Level("6|yfeAo6R8Wj$", 1), Level("byvZcF", 2), Level("owY[k", 1), Level("isChMWrYBGRde", 1), Level("_JJjeUFGh", 1), Level("EtyrG", 1), Level("aOyxW3|Vk:KB", 1), Level("w0u~W", 1)])
gRMzN= Factor("gRMzN", [Level("tdc", 1), Level("Jgu", 8), Level("NdStEO::}qAYo", 4), Level("XO12KQDACTWFC", 1), Level(":Vt", 1), Level("mnPru", 8), Level("hIiVtGGQK7Ag", 1), Level("Wvx!nW", 4)])

design=[OKJR_bFabtyQS,gRMzN]
crossing=[OKJR_bFabtyQS,gRMzN]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/8_3_1"))

### END
