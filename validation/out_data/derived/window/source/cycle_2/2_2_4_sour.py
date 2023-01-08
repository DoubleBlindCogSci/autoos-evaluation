from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
udcne = Factor("udcne", ["hhv","iyh","rncyt","xwfsc","auw","xdiee"])
ayqf = Factor("ayqf", ["sej","avz","dzzaj","rgqja","wqec","byccpl","gnfim"])
def rmjgfq(udcne, ayqf):
    return udcne[-1] == "rncyt" and ayqf[-3] != "rgqja"
def xtloa(udcne,ayqf):
    return not rmjgfq(udcne, ayqf)
xsz = Factor("qdcu", [DerivedLevel("ougyxb", Window(rmjgfq, [udcne, ayqf],4)), DerivedLevel("okdoat", Window(xtloa, [udcne, ayqf],4))])
### EXPERIMENT
design=[udcne,ayqf,xsz]
crossing=[xsz]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)