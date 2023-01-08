from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ircmk = Factor("ircmk", ["glw", "mbinxa"])
dhsgbr = Factor("dhsgbr", ["jbjy", "jby"])
rzrjz = Factor("rzrjz", ["hnspo", "ugwqst"])
wror = Factor("wror", ["qcezwo", "nzrc"])
constraints = []
crossing = [ircmk, dhsgbr, rzrjz, wror]


design=[ircmk,dhsgbr,rzrjz,wror]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3"))

### END