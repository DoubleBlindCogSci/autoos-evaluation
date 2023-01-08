from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tY_yFIsHZOb=[Level('CNgNhGHCCZHip',10),'kFEKuvBWnTg?3c',Level("YtThQKPVniM~",8),"Aq#{UhDtH"]
hQkbk=Factor('ZPWrVc',tY_yFIsHZOb)
VnLqZ='VQPBA'
OyOeSLNvG=Factor('eqGmUptsi',["oC7Sfpibdy",VnLqZ,Level('tJRJlVUb~yL',7),'VNZNo0p',"RBL5P?dedH"])
Y4ZebIu23=Factor("v}Vy",["2hy>",'MHU',Level('UwsYZMnPe',4),Level('ZMLL#T',2)])

### EXPERIMENT
design=[hQkbk,OyOeSLNvG,Y4ZebIu23]
crossing=[hQkbk,OyOeSLNvG,Y4ZebIu23]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3_0"))
### END