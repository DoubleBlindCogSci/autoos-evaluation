from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fep = Factor("fep", ["qfp", "lsiub"])
yyrhsx = Factor("yyrhsx", ["iks", "xvc"])
ilr = Factor("ilr", ["oimagt", "rxoxu"])
xnmjx = Factor("xnmjx", ["fvzixa", "gqvow"])
odk = Factor("odk", ["lurk", "jua"])
ofip = Factor("ofip", ["mht", "jfoeyb"])
zuzipw = Factor("zuzipw", ["sed", "dch"])

### EXPERIMENT
design=[fep,yyrhsx,ilr,xnmjx,odk,ofip,zuzipw]
crossing=[[fep,yyrhsx,ilr,xnmjx,odk,ofip,zuzipw]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_5"))
### END