from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
yytiv = Factor("yytiv", ["pek","csdat","iecoa","wmj","dounsc","mqkox","qmu"])
sjcll = Factor("sjcll", ["cxpc","uaflz","werkd","uaevq","qkmk","gbgkc"])
def msugnk(yytiv, sjcll):
    return yytiv == "qmu" or sjcll != "werkd"
def jhx(yytiv,sjcll):
    return yytiv != "qmu" and not (sjcll != "werkd")
vjsg = Factor("zmx", [DerivedLevel("fuldp", WithinTrial(msugnk, [yytiv, sjcll])), DerivedLevel("xopcn", WithinTrial(jhx, [yytiv, sjcll]))])
### EXPERIMENT
design=[yytiv,sjcll,vjsg]
crossing=[vjsg]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)