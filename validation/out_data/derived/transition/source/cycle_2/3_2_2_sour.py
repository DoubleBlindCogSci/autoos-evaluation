from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
zfr = Factor("zfr", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
whs = Factor("whs", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
amxjcp = Factor("amxjcp", ["hefubi","ykc","lexmh","hqijd","zicb","fwrian"])
def dhaeta(zfr, whs, amxjcp):
     return zfr[0] == whs[-1] and zfr[-1] != amxjcp[0]
def uqngx(zfr, whs, amxjcp):
     return whs[-1] != zfr[0] and amxjcp[0] == zfr[-1]
def qoyvvj(zfr, whs, amxjcp):
     return (not zfr[0] == whs[-1]) and (zfr[-1] != amxjcp[0])
edmv = Factor("srpb", [DerivedLevel("ahjve", Transition(dhaeta, [zfr, whs, amxjcp])), DerivedLevel("wtj", Transition(uqngx, [zfr, whs, amxjcp])),DerivedLevel("oasw", Transition(qoyvvj, [zfr, whs, amxjcp]))])
### EXPERIMENT
design=[zfr,whs,amxjcp,edmv]
crossing=[edmv]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)