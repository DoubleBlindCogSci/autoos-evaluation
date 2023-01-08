from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jKzX=Factor('UHiOjqnbU',[Level('rp1lOL#evEP3x',7),Level('T]Tjhxzd~',2),'hGqjd?wPSNcdq',"znsmPHpfA","^f;!","oE]lhEJxf",Level('lVUpk',1),'hJBMJ|g',"AJbGE"])
sahk4ycA3V='VMyuf}:$TQW'
AFJogAp=["BJSEyvvX","OkJ{O",Level('_QsjOpSwu(',2),'PpzE#N99U^RSMB','FnUpZw5aO%',Level('FfMi',7),'I%n',sahk4ycA3V,'YWy&]',Level('xKWkchXMInY',2)]
GrXPfeSP6=Factor("NjyastzmSRtAD",AFJogAp)
cHmXM7=Factor('HpsJeGNB',['8WM)BAZKaV',"&OfvK{",Level("TYZ",7),"Vz3X3yXZcA",'i_B',"DEAFokd",Level("wZJuZQSMLLOrgt",1),'CYwOs e]Rb','|k9z WS*VG~'])

### EXPERIMENT
design=[jKzX,GrXPfeSP6,cHmXM7]
crossing=[jKzX,GrXPfeSP6,cHmXM7]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_3_0"))
### END