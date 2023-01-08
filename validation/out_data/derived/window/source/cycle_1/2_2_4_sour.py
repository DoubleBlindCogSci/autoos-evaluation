from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
bxuppq = Factor("bxuppq", ["aeztdd","dfmej","qghegk","frl","xbd"])
ckg = Factor("ckg", ["eedo","hchmj","wgjcl","rjmyxh","ykcly"])
def vtlhke(bxuppq, ckg):
    return bxuppq[0] == "frl" and ckg[-3] == "eedo"
def ewcw(bxuppq,ckg):
    return bxuppq[0] != "frl" or not (ckg[-3] == "eedo")
fozwx = DerivedLevel("amfn", Window(vtlhke, [bxuppq, ckg],4))
dlebs = DerivedLevel("jyet", Window(ewcw, [bxuppq, ckg],4))
djkz = Factor("cal", [fozwx, dlebs])

### EXPERIMENT
design=[bxuppq,ckg,djkz]
crossing=[djkz]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)