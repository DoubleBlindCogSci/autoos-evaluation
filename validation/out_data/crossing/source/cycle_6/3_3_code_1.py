from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xyhn = Factor("xyhn", ["icwff", "nnf"])
rvrao = Factor("rvrao", ["rajkbb", "xzc"])
axio = Factor("axio", ["pwdgf", "wvt"])
yfbaat = Factor("yfbaat", ["ikexn", "bnevbc"])
mrgl = Factor("mrgl", ["xzqi", "loqbrj"])
qdg = Factor("qdg", ["isr", "exdeo"])
jiodvp = Factor("jiodvp", ["dlll", "fgg"])

### EXPERIMENT
design=[xyhn,rvrao,axio,yfbaat,mrgl,qdg,jiodvp]
crossing=[[xyhn,rvrao],[axio,yfbaat],[mrgl,qdg,jiodvp],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3"))
### END