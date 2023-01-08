from sweetpea import *
import os
_dir=os.path.dirname(__file__)
fep = Factor("fep", ["qfp", "lsiub"])
yyrhsx = Factor("yyrhsx", ["iks", "xvc"])
ilr = Factor("ilr", ["oimagt", "rxoxu"])
xnmjx = Factor("xnmjx", ["fvzixa", "gqvow"])
odk = Factor("odk", ["lurk", "jua"])
ofip = Factor("ofip", ["mht", "jfoeyb"])
zuzipw = Factor("zuzipw", ["sed", "dch"])
constraints = []
crossing = [fep, yyrhsx, ilr, xnmjx, odk, ofip, zuzipw]


design=[fep,yyrhsx,ilr,xnmjx,odk,ofip,zuzipw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_5"))

### END