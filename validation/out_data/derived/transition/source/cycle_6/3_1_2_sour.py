from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xatn = Factor("xatn", ["zzmnb","zqjdqg","agwq","opkof","lpx","fwxt","rhk"])
def epjo(xatn):
     return "rhk" == xatn[0] and xatn[-1] != "zqjdqg"
def dpmnri(xatn):
     return (not "rhk" != xatn[0]) and  xatn[-1] == "zqjdqg"
def jodp(xatn):
     return (not epjo(xatn)) and (not xatn[-1] == "zqjdqg")
grd = DerivedLevel("ftgjj", Transition(epjo, [xatn]))
xni = DerivedLevel("byul", Transition(dpmnri, [xatn]))
nxljwe = DerivedLevel("wuzutq", Transition(jodp, [xatn]))
wraa = Factor("lpnq", [grd, xni, nxljwe])

### EXPERIMENT
design=[xatn,wraa]
crossing=[wraa]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)