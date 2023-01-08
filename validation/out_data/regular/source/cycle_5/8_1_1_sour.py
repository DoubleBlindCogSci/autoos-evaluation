from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_RzJE=["qxS","F}Fv","QnmTo",'WAB 2;ZVH)f','NF?WtqD']
RCOXr=Factor("jGhkG",[' GyKQz6AtL','kHE^tK#PsSu','b6Cxtj{','dWZRHs SNQy5qt',"eMYNaS 9",':UhRc','yEhe]FrBMMhjn~',_RzJE[4],'I*LN '])

### EXPERIMENT
design=[RCOXr]
crossing=[RCOXr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_1_1_0.csv"))
nr_factors=1
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)