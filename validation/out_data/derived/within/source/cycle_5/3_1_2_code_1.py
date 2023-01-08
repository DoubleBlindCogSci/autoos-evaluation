from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xkj = Factor("xkj", ["ljiv","hitf","jctbq","savcm","gyed","cdrgmp","xynbu","anvp"])
def zbdf(xkj):
     return "savcm" == xkj
def hxqd(xkj):
     return "cdrgmp" == xkj
def twq(xkj):
     return (xkj != "savcm") and (xkj != "cdrgmp")
qzka = DerivedLevel("jshn", WithinTrial(zbdf, [xkj]))
ifve = DerivedLevel("ztvy", WithinTrial(hxqd, [xkj]))
dpvwra = DerivedLevel("enxao", WithinTrial(twq, [xkj]))
nlw = Factor("lssd", [qzka, ifve, dpvwra])

### EXPERIMENT
design=[xkj,nlw]
crossing=[nlw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END