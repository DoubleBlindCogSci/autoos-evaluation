from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rxh = Factor("rxh", ["yzi", "fqwrs"])
zvocuf = Factor("zvocuf", ["cmhub", "bebv"])
yvhe = Factor("yvhe", ["kjzw", "fijsg"])
wofih = Factor("wofih", ["rpvkm", "mmh"])

### EXPERIMENT
design=[rxh,zvocuf,yvhe,wofih]
crossing=[[rxh,zvocuf,yvhe,wofih]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_4"))
### END