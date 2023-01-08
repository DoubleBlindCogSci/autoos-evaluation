from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hwdb = Factor("hwdb", ["uhhgjg","wkwuq","qtj","igw","eoxdtw","dbss","sgw","grdt"])
gderh = Factor("gderh", ["uga","ziq","tswnb","mxgf","aqgxnv","hlx"])
def eduf(hwdb, gderh):
     return "eoxdtw" == hwdb[-1] and gderh[0] != "mxgf"
def qgv(hwdb, gderh):
     return hwdb[-1] != "eoxdtw" and gderh[0] == "mxgf"
def ezhwo(hwdb, gderh):
     return (not hwdb[-1] == "eoxdtw") and (not qgv(hwdb, gderh))
psef = Factor("xtw", [DerivedLevel("rjw", Transition(eduf, [hwdb, gderh])), DerivedLevel("wze", Transition(qgv, [hwdb, gderh])),DerivedLevel("iygzzo", Transition(ezhwo, [hwdb, gderh]))])
### EXPERIMENT
design=[hwdb,gderh,psef]
crossing=[psef]
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