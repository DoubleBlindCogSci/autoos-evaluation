from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
dqmt = Factor("dqmt", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
rqr = Factor("rqr", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
mxu = Factor("mxu", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
def xfoc(dqmt, rqr, mxu):
     return rqr[-2] == dqmt[-3]
def xmc(dqmt, rqr, mxu):
     return rqr[-2] != dqmt[-3] and mxu[-3] == dqmt[-2]
def onvo(dqmt, rqr, mxu):
     return (dqmt[-3] != rqr[-2]) and (dqmt[-2] != mxu[-3])
yngml = DerivedLevel("trma", Window(xfoc, [dqmt, rqr, mxu],4))
diseud = DerivedLevel("zvclql", Window(xmc, [dqmt, rqr, mxu],4))
xpciw = DerivedLevel("wpip", Window(onvo, [dqmt, rqr, mxu],4))
avy = Factor("gtv", [yngml, diseud, xpciw])

### EXPERIMENT
design=[dqmt,rqr,mxu,avy]
crossing=[avy]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)