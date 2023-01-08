from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
YE_ = Factor("YE<", [Level("{haV", 2), "YBZJBxV", "PDS", "WJHuH|rDXHnHUe", "hgdgZyj", "UJZ", "Rue", "exaZ"])
BTKTWe_kyCgvN = Factor("BTKTWe@kyCgvN", [Level("eFNXMVmtGQYl", 4), "}pY", "XoLR", "rvsjPXCGcnqdgg", "qzLkbpGUUwd", "^efYWfnP", "ssmIXo"])

design=[YE_,BTKTWe_kyCgvN]
crossing=[YE_,BTKTWe_kyCgvN]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_2_1"))

### END
