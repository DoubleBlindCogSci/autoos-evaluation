from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
flYUwZ=Factor("]bRxu?nA!A",['yh#SkZ$I',Level('Y%ou~IceHMu:Br',8),"SeBL","l}gPXP0i"])
lTq5=Factor('BBK]lP@nOHZ@Y',["FcPaPVVD;BuOtQ",'(nweqHF(hl',Level('GMJiBe',9),"wI7n6filLu"])

### EXPERIMENT
design=[flYUwZ,lTq5]
crossing=[flYUwZ,lTq5]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_2_0_0.csv"))
nr_factors=2
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)