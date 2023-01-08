from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jmz = Factor("jmz", ["jihy","vml","ualooh","zwib","okr","ltap"])
sqg = Factor("sqg", ["bxsq","cunuta","nxlob","vmuyd","ysq","xtn"])
def ves(jmz, sqg):
     return jmz[-1] == "jihy" and sqg[0] != "xtn"
def hzoqtd(jmz, sqg):
     return jmz[-1] != "jihy" and sqg[0] == "xtn"
def tjcetz(jmz, sqg):
     return (not jmz[-1] == "jihy") and (not sqg[0] == "xtn")
eiojv = Factor("zbhiv", [DerivedLevel("puhii", Transition(ves, [jmz, sqg])), DerivedLevel("wdcu", Transition(hzoqtd, [jmz, sqg])),DerivedLevel("kwuqg", Transition(tjcetz, [jmz, sqg]))])
### EXPERIMENT
design=[jmz,sqg,eiojv]
crossing=[eiojv]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)