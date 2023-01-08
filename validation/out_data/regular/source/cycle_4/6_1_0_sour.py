from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HEvoy7hdj=['zIM',"DY5","msr"]
RloV=Factor('pyOE~N7yFBpB',[Level('IDtdzk(QdMaMl',1),"wrbmtjn#CxL",'Q2Y','H&bDpC',':VAJHl${Lso','XmEcAJgQYMNJf',HEvoy7hdj[1]])

### EXPERIMENT
design=[RloV]
crossing=[RloV]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_0_0.csv"))
nr_factors=1
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)