from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
osey = Factor("osey", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
ndkbz = Factor("ndkbz", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
dwwn = Factor("dwwn", ["gdikt","kwfvqa","qhrj","nyvv","ciolxg"])
def ixy(osey, ndkbz, dwwn):
    return osey[0] != ndkbz[-1]
def kuyyd(osey, ndkbz, dwwn):
    return not ixy(osey, ndkbz, dwwn)
hfrr = DerivedLevel("gubi", Transition(ixy, [osey, ndkbz, dwwn]))
attvch = DerivedLevel("cdps", Transition(kuyyd, [osey, ndkbz, dwwn]))
xsu = Factor("pktwz", [hfrr, attvch])

### EXPERIMENT
design=[osey,ndkbz,dwwn,xsu]
crossing=[xsu]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)