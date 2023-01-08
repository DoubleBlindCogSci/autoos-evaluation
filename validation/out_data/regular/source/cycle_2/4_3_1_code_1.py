from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DLVLG7iZI0=Factor('UVq[fEbnWkk',[Level('KiLzF',5),'tiYQydlil>',"I13",Level('QMoi@D',7)])
Apuf=Factor("P3WfL]UX>iOyf",["DpD*VprHYcl","#Si!7ZG","dagYxP","AmTaWIpRQ"])
cRnfgItBL=Factor('cuuvWqk (x)RA',["ZTaZOVVLK",Level("IZ8",2),Level('3bB%KC3xHUf',3),'WSG;T>D5af{D4B'])

### EXPERIMENT
design=[DLVLG7iZI0,Apuf,cRnfgItBL]
crossing=[DLVLG7iZI0,Apuf,cRnfgItBL]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3_1"))
### END