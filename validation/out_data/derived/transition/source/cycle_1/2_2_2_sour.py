from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ljyd = Factor("ljyd", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
fxklzn = Factor("fxklzn", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
wykjm = Factor("wykjm", ["nvrrn","euo","svydy","gjj","kjppp","zwc"])
def entzqv(ljyd, wykjm, fxklzn):
    return ljyd[0] != wykjm[-1] or ljyd[-1] == fxklzn[0]
def ifaxww(ljyd, wykjm, fxklzn):
    return not entzqv(ljyd, wykjm, fxklzn)
qwcmdo = Factor("nhhng", [DerivedLevel("ubgi", Transition(entzqv, [ljyd, fxklzn, wykjm])), DerivedLevel("tiggrl", Transition(ifaxww, [ljyd, fxklzn, wykjm]))])
### EXPERIMENT
design=[ljyd,fxklzn,wykjm,qwcmdo]
crossing=[qwcmdo]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)