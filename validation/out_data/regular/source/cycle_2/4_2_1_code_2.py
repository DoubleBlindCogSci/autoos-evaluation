from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fiFAZYEF_ = Factor("fiFAZYEF7", [Level("n;u{", 10), Level("}JStvuEbR", 1), Level("ZVM", 3), Level("Oq z^{KPRkVf", 1)])
K_MYI_SMfSMnLr = Factor("K MYI4SMfSMnLr", [Level("YyV~klXy!K8Xf", 5), Level("G[N%:vgGnTw", 1), Level("yXrWqW}4[", 1), Level("|Pj", 1)])

design=[fiFAZYEF_,K_MYI_SMfSMnLr]
crossing=[fiFAZYEF_,K_MYI_SMfSMnLr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_1"))

### END
