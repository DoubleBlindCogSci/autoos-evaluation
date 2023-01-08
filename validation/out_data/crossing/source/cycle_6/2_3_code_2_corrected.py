from sweetpea import *
import os
_dir=os.path.dirname(__file__)
mkf = Factor("mkf", ["sputuy", "idp"])
mgzy = Factor("mgzy", ["xfz", "cec"])
constraints = []
crossing = [[mkf, mgzy],]


design=[mkf,mgzy]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3"))

### END
