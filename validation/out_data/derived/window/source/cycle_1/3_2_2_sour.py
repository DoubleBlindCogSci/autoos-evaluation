from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
mfz = Factor("mfz", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
jtrvnd = Factor("jtrvnd", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
zrs = Factor("zrs", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
def pit(mfz, zrs, jtrvnd):
     return zrs[-2] == mfz[-1]
def wgt(mfz, zrs, jtrvnd):
     return zrs[-2] != mfz[-1] and jtrvnd[-1] == mfz[-2]
def lmzmt(mfz, zrs, jtrvnd):
     return (not pit(mfz, zrs, jtrvnd)) and (not mfz[-2] == jtrvnd[-1])
rmabm = DerivedLevel("rap", Window(pit, [mfz, jtrvnd, zrs],3))
zbswp = DerivedLevel("gpksp", Window(wgt, [mfz, jtrvnd, zrs],3))
babh = DerivedLevel("xqjhvf", Window(lmzmt, [mfz, jtrvnd, zrs],3))
oudg = Factor("yaehve", [rmabm, zbswp, babh])

### EXPERIMENT
design=[mfz,jtrvnd,zrs,oudg]
crossing=[oudg]
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
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)