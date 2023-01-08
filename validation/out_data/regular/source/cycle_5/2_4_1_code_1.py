from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZxRxbYfQi5u='enhU|RVFM0'
UxTWTpqmCp=Factor('CGJ UZ(SM]Vw',['@ mxVsncjXSmU',ZxRxbYfQi5u,'GX;WW7'])
Li4DJ68l9U=Factor("Udyvgb*c",["Bg6ynwjKGthO",'Hv9{2^3cf0'])
JardxyGxrk=Factor('xEtS',[Level('PYm',2),Level("yJX",3)])
iqfqjBt=Factor('mdqtqldTz',["oDE<XPpz",'DHA)cR'])

### EXPERIMENT
design=[UxTWTpqmCp,Li4DJ68l9U,JardxyGxrk,iqfqjBt]
crossing=[UxTWTpqmCp,Li4DJ68l9U,JardxyGxrk,iqfqjBt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_4_1"))
### END