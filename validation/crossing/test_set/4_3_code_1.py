from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ircmk = Factor("ircmk", ["glw", "mbinxa"])
dhsgbr = Factor("dhsgbr", ["jbjy", "jby"])
rzrjz = Factor("rzrjz", ["hnspo", "ugwqst"])
wror = Factor("wror", ["qcezwo", "nzrc"])

### EXPERIMENT
design=[ircmk,dhsgbr,rzrjz,wror]
crossing=[[ircmk,dhsgbr,rzrjz,wror]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3"))
### END