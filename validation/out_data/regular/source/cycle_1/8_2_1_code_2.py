from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_D_b_bxWrwQ_= Factor("0D{b~bxWrwQ[", ["cEG|AN", "AxYZHAuaw:KhLA", "#ynLG<LYipZUi", "WWJYaXjVdZjk{", "gT (ibn|nvV", Level("ShtIhkGJAUZ>c", 10), "YD EuFMgoO", "AzRHf"])
__i= Factor("?^i", ["YDbPSaXjqFd(", Level("iwx", 6), "vOb2$Yfyz5", "5aZM<", "GQmm?Gq", Level("vRPsA)vO#7z", 10), Level("!vT", 1)])


design=[_D_b_bxWrwQ_,__i]
crossing=[_D_b_bxWrwQ_,__i]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/8_2_1"))

### END
