from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
swxrom = Factor("swxrom", ["indmsy","yrf","cwqp","ziaw","vhjh","irj","mdfvvh","cirqwl"])
hfo = Factor("hfo", ["rmn","jusbu","fyc","qcqre","uukbjl","akcut"])
def vld(swxrom, hfo):
     return "cwqp" == swxrom[-1] and not hfo[0] == "uukbjl"
def pedq(swxrom, hfo):
     return swxrom[-1] != "cwqp" and hfo[0] == "uukbjl"
def slvout(swxrom, hfo):
     return (not vld(swxrom, hfo)) and (not hfo[0] == "uukbjl")
aufk = Factor("ybt", [DerivedLevel("asygc", Transition(vld, [swxrom, hfo])), DerivedLevel("cgb", Transition(pedq, [swxrom, hfo])),DerivedLevel("chx", Transition(slvout, [swxrom, hfo]))])
### EXPERIMENT
design=[swxrom,hfo,aufk]
crossing=[aufk]
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