from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZBdW_si='kRtKnoE7XVWjvL'
js3bK23B=Factor("en gxxvL",[ZBdW_si,'OSPyW{fR',Level("FUWAO",1)])
y7_4Pfp2d=["g*iu",'CSaQw']
Dm6kohXX=Factor("PaGCajYpIEehuq",y7_4Pfp2d)
V353f0TROt=Factor("E[_elRfqN",[Level("U[x?obejL%",8),"yjOmrT"])

### EXPERIMENT
design=[js3bK23B,Dm6kohXX,V353f0TROt]
crossing=[js3bK23B,Dm6kohXX,V353f0TROt]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_3_0_0.csv"))
nr_factors=3
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)