from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
wsle = Factor("wsle", ["jerlq","dthqsq","hpuvln","sorijz","zwze","nxcmu","amrfiy","oemibc"])
def aly(wsle):
     return "sorijz" == wsle[0]
def iaun(wsle):
     return wsle[-1] == "jerlq"
def xxtxnd(wsle):
     return (not wsle[0] == "sorijz") and (not iaun(wsle))
owbhqo = Factor("zhyw", [DerivedLevel("zldik", Transition(aly, [wsle])), DerivedLevel("oflt", Transition(iaun, [wsle])),DerivedLevel("ziowfh", Transition(xxtxnd, [wsle]))])
### EXPERIMENT
design=[wsle,owbhqo]
crossing=[owbhqo]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)