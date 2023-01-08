from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zgzyu = Factor("zgzyu", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
myuanw = Factor("myuanw", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
mpvcn = Factor("mpvcn", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
def xsx(zgzyu, mpvcn, myuanw):
    return zgzyu[0] != mpvcn[-1] and zgzyu[-1] != myuanw[0]
def himr(zgzyu, mpvcn, myuanw):
    return not (zgzyu[0] != mpvcn[-1]) or not (zgzyu[-1] != myuanw[0])
gxatcd = Factor("urgjg", [DerivedLevel("eqi", Transition(xsx, [zgzyu, myuanw, mpvcn])), DerivedLevel("cqtu", Transition(himr, [zgzyu, myuanw, mpvcn]))])
### EXPERIMENT
design=[zgzyu,myuanw,mpvcn,gxatcd]
crossing=[gxatcd]
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