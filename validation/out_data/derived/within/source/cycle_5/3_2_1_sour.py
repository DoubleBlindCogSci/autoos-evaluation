from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pveal = Factor("pveal", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
axewwo = Factor("axewwo", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
xwxcp = Factor("xwxcp", ["xsqkdq","iwf","bcnq","tybbmf","abasur","hty","acego"])
def tfk(pveal, xwxcp, axewwo):
     return pveal == xwxcp
def hkb(pveal, xwxcp, axewwo):
     return xwxcp != pveal and pveal == axewwo
def pcrh(pveal, xwxcp, axewwo):
     return (pveal != xwxcp) and (not pveal == axewwo)
mkscp = Factor("ipe", [DerivedLevel("aopz", WithinTrial(tfk, [pveal, axewwo, xwxcp])), DerivedLevel("abbfb", WithinTrial(hkb, [pveal, axewwo, xwxcp])),DerivedLevel("pcwrkd", WithinTrial(pcrh, [pveal, axewwo, xwxcp]))])
### EXPERIMENT
design=[pveal,axewwo,xwxcp,mkscp]
crossing=[mkscp]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)