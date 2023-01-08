from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
vxqndv = Factor("vxqndv", ["egnpd","aof","ybec","jcamd","gocgh","qcdyxn"])
def fnr(vxqndv):
     return vxqndv[-2] == "jcamd"
def wbfb(vxqndv):
     return "egnpd" == vxqndv[0]
def ayno(vxqndv):
     return (vxqndv[-2] != "jcamd") and (not wbfb(vxqndv))
innvkv = Factor("tyruji", [DerivedLevel("kbpq", Window(fnr, [vxqndv],3)), DerivedLevel("bmb", Window(wbfb, [vxqndv],3)),DerivedLevel("nfzkw", Window(ayno, [vxqndv],3))])
### EXPERIMENT
design=[vxqndv,innvkv]
crossing=[innvkv]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)