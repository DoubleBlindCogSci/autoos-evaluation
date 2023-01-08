from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gqjsay = Factor("gqjsay", ["kgay", "vuabd"])
ylp = Factor("ylp", ["ioatiu", "imsulx"])
gmyjy = Factor("gmyjy", ["bhc", "dcz"])
wjs = Factor("wjs", ["hbi", "bhjvs"])
waezh = Factor("waezh", ["uqc", "wtz"])
aix = Factor("aix", ["cncejk", "baj"])
egmwc = Factor("egmwc", ["ifen", "vwufe"])
jmj = Factor("jmj", ["kverk", "ebnt"])

### EXPERIMENT
design=[gqjsay,ylp,gmyjy,wjs,waezh,aix,egmwc,jmj]
crossing=[[gqjsay,ylp,gmyjy],[wjs,waezh,aix,egmwc],[jmj],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3"))
### END