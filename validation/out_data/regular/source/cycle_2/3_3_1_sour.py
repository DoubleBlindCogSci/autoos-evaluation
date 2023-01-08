from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
CV3I=Factor('ZdkRbRp:P',[Level('Fb7dSvHvCg Ga',8),'Eiy]ly',Level('}3QL',3)])
vG8op_mxAt=Factor('p1KMSdDk',[Level('HONKDt',3),'OHitE','YU f'])
HsP2k3vmS=["5zJZXXSWn",Level('%J7MvI3',9),"TspfX"]
PXmk_=Factor('La^0wTd^4iQ',HsP2k3vmS)

### EXPERIMENT
design=[CV3I,vG8op_mxAt,PXmk_]
crossing=[CV3I,vG8op_mxAt,PXmk_]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_3_1_0.csv"))
nr_factors=3
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)