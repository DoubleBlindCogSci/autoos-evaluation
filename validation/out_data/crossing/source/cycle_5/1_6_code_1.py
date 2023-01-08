from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
efoaam = Factor("efoaam", ["vaw", "jytf"])
kouhiu = Factor("kouhiu", ["pswae", "pcl"])

### EXPERIMENT
design=[efoaam,kouhiu]
crossing=[[efoaam,kouhiu],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_6"))
### END