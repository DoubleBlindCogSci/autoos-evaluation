from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jpbHno=['%Z}',Level('yaw',3),'OOab$%JUR','LYT',"hheFg",'YRwAXw',Level("~xxjZEUaIbqR6",4),"VAAiZx"]
DfWTiUtL1C5=Factor('nojea7nz7?Eb',jpbHno)
Krs7MlXkZp=Factor('!>gupuVfSeK',['PfTiRZJWRrX^u','qKMAU','qLX~v','Q(L(FafcBoR ','FCSk;oW','blu',"OR SOfdt0aKE",'VJ&HI~LLdmaRD'])
rvqg0Yu=[Level('3Q|9',2),'?gTNAXGea&',Level('qYYY',2),"aoJ3","qlZO$txitrcnc",'FDJf',"f;iW@bs","s9LfnOlKQpFt"]
uAYwTIDTx=Factor("qBnJwyqc",rvqg0Yu)

### EXPERIMENT
design=[DfWTiUtL1C5,Krs7MlXkZp,uAYwTIDTx]
crossing=[DfWTiUtL1C5,Krs7MlXkZp,uAYwTIDTx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_3_0"))
### END