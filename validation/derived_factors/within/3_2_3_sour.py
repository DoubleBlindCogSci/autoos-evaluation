from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cfs = Factor("cfs", ["unbwah","hidt","muml","opnyde","jrt","wqptl","xtj","iwmwm"])
ytg = Factor("ytg", ["unbwah","hidt","muml","opnyde","jrt","wqptl","xtj","iwmwm"])
gjruka = Factor("gjruka", ["unbwah","hidt","muml","opnyde","jrt","wqptl","xtj","iwmwm"])
def khyzg(cfs, gjruka, ytg):
     return cfs == gjruka
def jfnhpi(cfs, gjruka, ytg):
     return gjruka != cfs and ytg == cfs
def njxe(cfs, gjruka, ytg):
     return (cfs != gjruka) and (not jfnhpi(cfs, gjruka, ytg))
mozr = DerivedLevel("gntah", WithinTrial(khyzg, [cfs, ytg, gjruka]))
lcex = DerivedLevel("wbey", WithinTrial(jfnhpi, [cfs, ytg, gjruka]))
vvkpsu = DerivedLevel("wtug", WithinTrial(njxe, [cfs, ytg, gjruka]))
aca = Factor("agrgs", [mozr, lcex, vvkpsu])

### EXPERIMENT
design=[cfs,ytg,gjruka,aca]
crossing=[aca]
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