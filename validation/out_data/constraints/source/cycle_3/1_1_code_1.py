from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pzsn = Factor("pzsn", ["fft","yij","nsk", "mtlfsy"])
bqb = Factor("bqb", ["frefdz","eexquv", "wqi"])
bje = Factor("bje", ["plgqjm","ubuecw", "vun"])

### EXPERIMENT
constraints=[MinimumTrials(18)]
design=[pzsn,bqb,bje]
crossing=[bqb,bje]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_1"))
### END