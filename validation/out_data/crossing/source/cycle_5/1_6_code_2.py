from sweetpea import *
import os
_dir=os.path.dirname(__file__)
efoaam = Factor("efoaam", ["vaw", "jytf"])
kouhiu = Factor("kouhiu", ["pswae", "pcl"])
constraints = []
crossing = [efoaam, kouhiu]


design=[efoaam,kouhiu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_6"))

### END