from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nany4KTW=Factor('}IhWtp$mZHNk',['xVKcYBsM',"ujqZpsU<",Level('rYi[QKIPh%',2),'X)jVF;BFQpOfZx','BdWL9jGhcQq&A'])
O3A7jDA2s="tDRYJzM5F6OV6"
ZmurPJrFB=Factor("|8mOqqZEHfJb",[" ZOhm",'roW#sIF_',"b$QSXbD",'jlTd7z',"TZs",O3A7jDA2s])

### EXPERIMENT
design=[nany4KTW,ZmurPJrFB]
crossing=[nany4KTW,ZmurPJrFB]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_1"))
### END