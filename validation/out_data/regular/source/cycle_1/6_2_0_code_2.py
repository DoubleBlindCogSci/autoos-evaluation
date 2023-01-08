from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jUf_GSNjsdU_E_= Factor("jUf;GSNjsdU<E?", [Level("wsnZnqLWlD", 1), Level("a$tmZO", 1), Level("EL(zDtnWikAAw", 1), Level("TMm5ZB", 1), Level("CzhjVwxjc1?cbV", 1), Level("rPfCErTNe", 3)])
BRpwg_n= Factor("BRpwg n", [Level("]^F", 1), Level("8bdJ", 1), Level("w_e};^C@NPhWM", 1), Level("TnOQoUDtN", 5), Level("]QCdmJ", 1), Level(";gMlwG", 1)])

design=[jUf_GSNjsdU_E_,BRpwg_n]
crossing=[jUf_GSNjsdU_E_,BRpwg_n]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/6_2_0"))

### END
