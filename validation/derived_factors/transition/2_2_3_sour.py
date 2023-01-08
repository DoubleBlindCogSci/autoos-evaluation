from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hbrcki = Factor("hbrcki", ["mwkocn","oivj","xmbdsc","wdoqku","jmvfq"])
hbasyw = Factor("hbasyw", ["mwkocn","oivj","xmbdsc","wdoqku","jmvfq"])
dfp = Factor("dfp", ["mwkocn","oivj","xmbdsc","wdoqku","jmvfq"])
def wtzm(hbrcki, dfp, hbasyw):
    return hbrcki[0] != dfp[-1] and hbrcki[-1] != hbasyw[0]
def yye(hbrcki, dfp, hbasyw):
    return not wtzm(hbrcki, dfp, hbasyw)
opb = Factor("lccd", [DerivedLevel("ssyqzm", Transition(wtzm, [hbrcki, hbasyw, dfp])), DerivedLevel("hxmnd", Transition(yye, [hbrcki, hbasyw, dfp]))])
### EXPERIMENT
design=[hbrcki,hbasyw,dfp,opb]
crossing=[opb]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)