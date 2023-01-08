from sweetpea import *
import os
_dir=os.path.dirname(__file__)
xyhn = Factor("xyhn", ["icwff", "nnf"])
rvrao = Factor("rvrao", ["rajkbb", "xzc"])
axio = Factor("axio", ["pwdgf", "wvt"])
yfbaat = Factor("yfbaat", ["ikexn", "bnevbc"])
mrgl = Factor("mrgl", ["xzqi", "loqbrj"])
qdg = Factor("qdg", ["isr", "exdeo"])
jiodvp = Factor("jiodvp", ["dlll", "fgg"])
constraints = []
crossing = [[xyhn, rvrao], [axio, yfbaat], [mrgl, qdg, jiodvp]]


design=[xyhn,rvrao,axio,yfbaat,mrgl,qdg,jiodvp]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3"))

### END