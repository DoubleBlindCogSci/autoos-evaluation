from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
lnc = Factor("lnc", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
ziyuus = Factor("ziyuus", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
fpj = Factor("fpj", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
def hzrcms(lnc, ziyuus, fpj):
    return lnc[-1] != ziyuus[0]
def jdk(lnc, ziyuus, fpj):
    return lnc[-1] == ziyuus[0]
gubqwb = Factor("dsny", [DerivedLevel("hxibgp", Window(hzrcms, [lnc, ziyuus, fpj],2)), DerivedLevel("cbvbbo", Window(jdk, [lnc, ziyuus, fpj],2))])
### EXPERIMENT
design=[lnc,ziyuus,fpj,gubqwb]
crossing=[gubqwb]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/2_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/2_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)