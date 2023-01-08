from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
YgtsvYET = Factor("YgtsvYET", ["LX6wnk", "ylO", "6SyYjHVgKmk", "BC~UhxQyIEw"])
etcI = Factor("etcI", [Level("lxGOK", 4), "opEjNb zCdxUu(", "pVcP)ui{l$w", "5[Q7PR"])

design=[YgtsvYET,etcI]
crossing=[YgtsvYET,etcI]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_0"))

### END
