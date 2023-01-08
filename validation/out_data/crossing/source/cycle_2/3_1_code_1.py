from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xus = Factor("xus", ["jidj", "wiqy"])
aqxogw = Factor("aqxogw", ["culmql", "vncenr"])
gfauq = Factor("gfauq", ["ygxxx", "zacq"])
jok = Factor("jok", ["priu", "yukw"])
wgfvtm = Factor("wgfvtm", ["umjh", "wieqwy"])
pvzvld = Factor("pvzvld", ["jjsvw", "isl"])

### EXPERIMENT
design=[xus,aqxogw,gfauq,jok,wgfvtm,pvzvld]
crossing=[[xus,aqxogw,gfauq],[jok,wgfvtm],[pvzvld],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1"))
### END