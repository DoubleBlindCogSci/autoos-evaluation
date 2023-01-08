from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
siPi=Factor('Clt[CF',["l22dmT|iW[Wa",'IcuLjigs?8',Level('rh;nbLysFxfYop',3),Level('aWL',6)])
aSb3xlnA0=Factor("P|J%L^y",[Level(";oKZhQWhvC",1),'rqF^P;v0I',Level('#iMgXnO:',6),Level('PVWYarfX',3)])

### EXPERIMENT
design=[siPi,aSb3xlnA0]
crossing=[siPi,aSb3xlnA0]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_1_0.csv"))
nr_factors=2
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)