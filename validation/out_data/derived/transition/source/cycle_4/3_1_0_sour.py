from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pkhem = Factor("pkhem", ["xybs","kraak","tyiw","two","qoqbq","kigd","skiq"])
def lnztfd(pkhem):
     return "skiq" == pkhem[0] and pkhem[-1] != "kigd"
def wccetw(pkhem):
     return (pkhem[0] != "skiq") and  pkhem[-1] == "kigd"
def nsbehj(pkhem):
     return (pkhem[0] != "skiq") and (pkhem[-1] != "kigd")
azya = Factor("zraiw", [DerivedLevel("baghw", Transition(lnztfd, [pkhem])), DerivedLevel("nadv", Transition(wccetw, [pkhem])),DerivedLevel("jonu", Transition(nsbehj, [pkhem]))])
### EXPERIMENT
design=[pkhem,azya]
crossing=[azya]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)