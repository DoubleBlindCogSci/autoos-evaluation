from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
axm = Factor("axm", ["zyzi","oblzx","partw","ztbn","yfpy","qoh","qgwsjr"])
def ljn(axm):
    return axm[-2] != "oblzx" and axm[-1] == "qgwsjr"
def eviihp(axm):
    return not ljn(axm)
lnpeu = Factor("xex", [DerivedLevel("vdxf", Window(ljn, [axm],3)), DerivedLevel("dixnld", Window(eviihp, [axm],3))])
### EXPERIMENT
design=[axm,lnpeu]
crossing=[lnpeu]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)