from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
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
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_3_0_0.csv"))
nr_factors=3
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)