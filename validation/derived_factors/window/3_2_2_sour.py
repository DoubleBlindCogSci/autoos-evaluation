from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iwp = Factor("iwp", ["jpx","ldmbjp","nyocl","eez","nxwmx","xkdgn"])
hbo = Factor("hbo", ["qyqzgn","mdk","eep","kerur","duc","bbidzv"])
def cgtvge(iwp, hbo):
     return iwp[-2] == "xkdgn" and hbo[-1] != "qyqzgn"
def qhlyvw(iwp, hbo):
     return "xkdgn" != iwp[-2] and  hbo[-1] == "qyqzgn"
def jdj(iwp, hbo):
     return (iwp[-2] != "xkdgn") and (not qhlyvw(iwp, hbo))
wqc = Factor("wfq", [DerivedLevel("wcu", Window(cgtvge, [iwp, hbo],3,1)), DerivedLevel("dbxyui", Window(qhlyvw, [iwp, hbo],3,1)),DerivedLevel("wwtvi", Window(jdj, [iwp, hbo],3,1))])
### EXPERIMENT
design=[iwp,hbo,wqc]
crossing=[wqc]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)