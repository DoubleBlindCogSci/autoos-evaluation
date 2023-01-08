from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eocrk = Factor("eocrk", ["jjf", "yoths"])
mjyi = Factor("mjyi", ["glwnq", "bpprhp"])
xbbvv = Factor("xbbvv", ["oukd","oopby","byxzg", "raw"])

### EXPERIMENT
constraints=[ExactlyK(2,(eocrk,"yoths"))]
design=[eocrk,mjyi,xbbvv]
crossing=[mjyi,xbbvv]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_3"))
### END