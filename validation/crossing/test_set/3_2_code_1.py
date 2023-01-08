from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
droiw = Factor("droiw", ["qfif", "swy"])
ijqht = Factor("ijqht", ["gdurqo", "wicba"])
vooe = Factor("vooe", ["gdf", "rrnukm"])

### EXPERIMENT
design=[droiw,ijqht,vooe]
crossing=[[droiw,ijqht,vooe]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END