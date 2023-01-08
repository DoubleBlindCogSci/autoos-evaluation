from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mkf = Factor("mkf", ["sputuy", "idp"])
mgzy = Factor("mgzy", ["xfz", "cec"])

### EXPERIMENT
design=[mkf,mgzy]
crossing = [[mgzy],[mkf],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3"))
### END
