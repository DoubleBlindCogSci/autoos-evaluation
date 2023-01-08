from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
FRep = Factor("FRep", [Level("kQEFiiw|6lz7", 1), Level("fLMdM S", 6)])
dqWvEw__ke_f = Factor("dqWvEw;1ke&f", ["VcYd7Fh", "RPd9xPS"])
_HMqbAriUXtgR = Factor("5HMqbAriUXtgR", ["rrsZ", "MaocZJZr:KI"])

design=[FRep,dqWvEw__ke_f,_HMqbAriUXtgR]
crossing=[FRep,dqWvEw__ke_f,_HMqbAriUXtgR]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3_0"))

### END
