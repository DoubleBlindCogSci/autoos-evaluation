from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kbyad = Factor("kbyad", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
jrnzbu = Factor("jrnzbu", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
yepn = Factor("yepn", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
def wwlarp(kbyad, yepn, jrnzbu):
     return kbyad[0] == yepn[-1] and kbyad[-1] != jrnzbu[0]
def qfjsp(kbyad, yepn, jrnzbu):
     return yepn[-1] != kbyad[0] and jrnzbu[0] == kbyad[-1]
def yvfkk(kbyad, yepn, jrnzbu):
     return (not kbyad[0] == yepn[-1]) and (not kbyad[-1] == jrnzbu[0])
rthi = DerivedLevel("qwwz", Transition(wwlarp, [kbyad, jrnzbu, yepn]))
aji = DerivedLevel("zqmb", Transition(qfjsp, [kbyad, jrnzbu, yepn]))
zgr = DerivedLevel("yqqnsu", Transition(yvfkk, [kbyad, jrnzbu, yepn]))
kjrfds = Factor("ylp", [rthi, aji, zgr])

### EXPERIMENT
design=[kbyad,jrnzbu,yepn,kjrfds]
crossing=[kjrfds]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)