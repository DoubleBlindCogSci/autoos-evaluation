from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VMbHH = Factor("VMbHH", ["yTsQ", "EBZV&^OQU", "EEYubd;GPul8b", "xCN", "QDMR", "@lC#OBcnWUD"])
Wcax = Factor("Wcax", ["LzEJdsI", "MK2WDcS", "hQWiXO5r", "WicY", "pG9", "coO]"])

design=[VMbHH,Wcax]
crossing=[VMbHH,Wcax]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_0"))

### END
