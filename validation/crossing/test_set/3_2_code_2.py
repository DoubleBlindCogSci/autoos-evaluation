from sweetpea import *
import os
_dir=os.path.dirname(__file__)
droiw = Factor("droiw", ["qfif", "swy"])
ijqht = Factor("ijqht", ["gdurqo", "wicba"])
vooe = Factor("vooe", ["gdf", "rrnukm"])
constraints = []
crossing = [droiw, ijqht, vooe]


design=[droiw,ijqht,vooe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2"))

### END