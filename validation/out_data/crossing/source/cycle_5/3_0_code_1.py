from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xhdcky = Factor("xhdcky", ["hms", "jpl"])
ddxcwv = Factor("ddxcwv", ["req", "yilhah"])
brzk = Factor("brzk", ["fwsjm", "mylmfg"])
szxhha = Factor("szxhha", ["hfnddc", "uzkce"])
emsmh = Factor("emsmh", ["jjfa", "jjmz"])
ypecf = Factor("ypecf", ["zbv", "mkl"])
fkuvc = Factor("fkuvc", ["vyvi", "dghqnf"])

### EXPERIMENT
design=[xhdcky,ddxcwv,brzk,szxhha,emsmh,ypecf,fkuvc]
crossing=[[xhdcky,ddxcwv,brzk],[szxhha,emsmh,ypecf],[fkuvc],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_0"))
### END