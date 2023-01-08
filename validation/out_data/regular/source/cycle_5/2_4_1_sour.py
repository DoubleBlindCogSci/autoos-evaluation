from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
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
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_4_1_0.csv"))
nr_factors=4
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)