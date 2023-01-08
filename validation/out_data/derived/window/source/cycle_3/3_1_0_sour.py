from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wjnax = Factor("wjnax", ["wlxyd","zrql","xmrrwb","hsq","vncl","etbr"])
def bwfz(wjnax):
     return wjnax[0] == "xmrrwb" and not wjnax[-3] == "xmrrwb"
def wsfrj(wjnax):
     return wjnax[0] != "xmrrwb" and  wjnax[-3] == "vncl"
def ybn(wjnax):
     return (wjnax[0] != "xmrrwb") and (not wsfrj(wjnax))
jinl = DerivedLevel("noxy", Window(bwfz, [wjnax],4))
vvchk = DerivedLevel("joc", Window(wsfrj, [wjnax],4))
vvrhv = DerivedLevel("bwit", Window(ybn, [wjnax],4))
ewdyz = Factor("samck", [jinl, vvchk, vvrhv])

### EXPERIMENT
design=[wjnax,ewdyz]
crossing=[ewdyz]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)