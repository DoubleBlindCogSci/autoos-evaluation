from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sZxB_k_= Factor("sZxB)k(", [Level("Zkx", 1), Level("dKWtWQrOAQFfz", 1), Level("%>QH:WjhvIM", 1), Level("S$ OwGDsUW", 1), Level("BPNO[Gkigk", 8), Level("0viLZCm<qsj", 1), Level("QxDuSEy", 1), Level("E|YHXMn8ONxhIR", 1)])
hrYqFG= Factor("hrYqFG", [Level("ZrF", 1), Level("r*a3yhl^t", 6), Level("&HdXvp]dcIM", 1), Level("lQTwqZ", 1), Level("lJA5tcEWomCqB", 10), Level("kzZKEWr^v", 1), Level("lJrxL(BNChimdM", 1)])
CTb= Factor("CTb", [Level("Qzq", 1), Level("MCjEVcQ!~z~5V", 1), Level("sNWxfAx(L]Sv", 9), Level("yCYNI", 1), Level("%se2nV", 1), Level("IPeluGRK4I", 1), Level("rex@G|y8{vpxPD", 1)])

design=[sZxB_k_,hrYqFG,CTb]
crossing=[sZxB_k_,hrYqFG,CTb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/7_3_1"))

### END
