from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
dwrpg = Factor("dwrpg", ["kjdt","syccui","nuzuca","jbwexv","fayn","vut"])
ossys = Factor("ossys", ["jvvyw","xru","juns","bct","slm","gunfs","rijlq","mykt"])
def sifpqk(dwrpg, ossys):
     return "kjdt" == dwrpg[-1]
def jjuqdb(dwrpg, ossys):
     return dwrpg[-1] != "kjdt" and  ossys[0] == "juns"
def fhqe(dwrpg, ossys):
     return (not sifpqk(dwrpg, ossys)) and (not ossys[0] == "juns")
ojhtof = DerivedLevel("zphjm", Transition(sifpqk, [dwrpg, ossys]))
gxl = DerivedLevel("cgtyi", Transition(jjuqdb, [dwrpg, ossys]))
fdg = DerivedLevel("ugeqmm", Transition(fhqe, [dwrpg, ossys]))
hldz = Factor("itia", [ojhtof, gxl, fdg])

### EXPERIMENT
design=[dwrpg,ossys,hldz]
crossing=[hldz]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)