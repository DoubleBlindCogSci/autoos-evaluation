from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hstuwb = Factor("hstuwb", ["leuc","epe","vtgmh","grktu","lzciwx","slzolh"])
zfln = Factor("zfln", ["ydiyqj","nhj","rld","llh","dnsu","qiwv"])
def xow(hstuwb, zfln):
     return hstuwb[-1] == "slzolh" and not zfln[0] == "ydiyqj"
def apz(hstuwb, zfln):
     return hstuwb[-1] != "slzolh" and zfln[0] == "ydiyqj"
def fqdi(hstuwb, zfln):
     return (not hstuwb[-1] == "slzolh") and (not apz(hstuwb, zfln))
tvzj = Factor("eqm", [DerivedLevel("fbhrc", Transition(xow, [hstuwb, zfln])), DerivedLevel("thwl", Transition(apz, [hstuwb, zfln])),DerivedLevel("ixo", Transition(fqdi, [hstuwb, zfln]))])
### EXPERIMENT
design=[hstuwb,zfln,tvzj]
crossing=[tvzj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)