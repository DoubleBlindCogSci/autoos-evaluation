from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nyy = Factor("nyy", ["jjsaj","fzzu","nkgyi","paixu","wbgk","vwtci"])
eqgxv = Factor("eqgxv", ["wbz","ugcj","addimm","tidq","kfdsc","xuyt","vjgv"])
def vddugg(nyy, eqgxv):
     return "fzzu" == nyy[-1] and eqgxv[0] != "xuyt"
def sqq(nyy, eqgxv):
     return "fzzu" != nyy[-1] and eqgxv[0] == "xuyt"
def hda(nyy, eqgxv):
     return (not nyy[-1] == "fzzu") and (not sqq(nyy, eqgxv))
unrc = DerivedLevel("gzuju", Transition(vddugg, [nyy, eqgxv]))
mqdef = DerivedLevel("wvbiev", Transition(sqq, [nyy, eqgxv]))
iayp = DerivedLevel("iaqvaw", Transition(hda, [nyy, eqgxv]))
zfqw = Factor("roau", [unrc, mqdef, iayp])

### EXPERIMENT
design=[nyy,eqgxv,zfqw]
crossing=[zfqw]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)