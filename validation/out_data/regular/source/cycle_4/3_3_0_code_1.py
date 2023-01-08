from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xyfFL=["uhUXnEXCs8HyfK","pvE!bQ>UONI6y","AnkCSis)xOlIC"]
nOdlgJp4=Factor(';pkr{EXiq',xyfFL)
IFqGrh=Factor('zdo',['Urj1gZikPN','MiU','U~d@SfnHGS'])
TtEuhEoTK7c=Factor('mF9KSYGW',['KYAxQO','Iry1Asyr; ;Gy',"DLJOkI"])

### EXPERIMENT
design=[nOdlgJp4,IFqGrh,TtEuhEoTK7c]
crossing=[nOdlgJp4,IFqGrh,TtEuhEoTK7c]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3_0"))
### END