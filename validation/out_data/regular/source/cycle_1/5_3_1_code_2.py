from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hDgQWaXpJJ_Z= Factor("hDgQWaXpJJ6Z", [Level("Zqh)C1x", 1), Level("mt]IDVYR@UZH", 9), Level("fMKmyzbf", 1), Level("DELscRU#P|utl}", 1), Level("fC>DXcdXJQMjhm", 1)])
wGgWr= Factor("wGgWr", [Level("SNL", 9), Level("FSH", 1), Level("cxlmR", 1), Level("enWvs]SdPQfU", 2), Level("FMyr_g3lEfn", 10), Level("pXBiAxc|", 1)])
ynYzCPvL_mPs= Factor("ynYzCPvL%mPs", [Level("dQstz?fp)Um", 1), Level("CziVPGnK", 1), Level("Kpt", 1), Level("kyhQSeMg", 4), Level("jtcK", 1)])

design=[hDgQWaXpJJ_Z,wGgWr,ynYzCPvL_mPs]
crossing=[hDgQWaXpJJ_Z,wGgWr,ynYzCPvL_mPs]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/5_3_1"))

### END
