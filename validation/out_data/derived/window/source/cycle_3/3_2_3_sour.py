from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xzar = Factor("xzar", ["czr","kradd","einxyr","anxmad","yrfr","xdmei","jhpjrv","jix"])
fnhg = Factor("fnhg", ["ooollz","zrxn","brvdut","fybb","whgo","zigtjm","toz"])
def wunm(xzar, fnhg):
     return "jhpjrv" == xzar[0] and not fnhg[-2] == "zigtjm"
def wfhhd(xzar, fnhg):
     return xzar[0] != "jhpjrv" and  fnhg[-2] == "zigtjm"
def pxfzbu(xzar, fnhg):
     return (not wunm(xzar, fnhg)) and (not wfhhd(xzar, fnhg))
expra = Factor("svpnhe", [DerivedLevel("vkj", Window(wunm, [xzar, fnhg],3)), DerivedLevel("xkghzg", Window(wfhhd, [xzar, fnhg],3)),DerivedLevel("dxo", Window(pxfzbu, [xzar, fnhg],3))])
### EXPERIMENT
design=[xzar,fnhg,expra]
crossing=[expra]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)