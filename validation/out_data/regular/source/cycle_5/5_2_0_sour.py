from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OA3zy7i84R8=Factor("5JrGsjQS0ac",['$QmMKda',"uFqH~NdBPvw","bPM",'zyM','OIBgN'])
YtyK12=Factor("OMsoAsh!VrtU",["lq!Ez",'rqevcqq<N',"bxcdB","x:a2WsaUMC>;Yj","T?jq"])

### EXPERIMENT
design=[OA3zy7i84R8,YtyK12]
crossing=[OA3zy7i84R8,YtyK12]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_0_0.csv"))
nr_factors=2
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)