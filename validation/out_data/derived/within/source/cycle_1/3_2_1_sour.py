from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
taaa = Factor("taaa", ["filhdf","zmdo","nexxd","fpsq","ysn","gjlyl","cspkuu","msxd"])
vcz = Factor("vcz", ["uwleue","xuceqb","abux","dtfovj","bio","fus","uxtm"])
def uhjc(taaa, vcz):
     return taaa == "filhdf"
def barkmp(taaa, vcz):
     return taaa != "filhdf" and  vcz == "bio"
def ynb(taaa, vcz):
     return (taaa != "filhdf") and (not barkmp(taaa, vcz))
hxjww = DerivedLevel("ajplpx", WithinTrial(uhjc, [taaa, vcz]))
wmeygd = DerivedLevel("mlkbl", WithinTrial(barkmp, [taaa, vcz]))
wpqxo = DerivedLevel("dosx", WithinTrial(ynb, [taaa, vcz]))
woyyf = Factor("djwavc", [hxjww, wmeygd, wpqxo])

### EXPERIMENT
design=[taaa,vcz,woyyf]
crossing=[woyyf]
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