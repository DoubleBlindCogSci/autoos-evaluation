from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mkepe = Factor("mkepe", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
ytw = Factor("ytw", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
nbv = Factor("nbv", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
def kwoas(mkepe, ytw, nbv):
     return ytw[-1] == mkepe[0] and mkepe[-1] != nbv[0]
def vvx(mkepe, ytw, nbv):
     return ytw[-1] != mkepe[0] and mkepe[-1] == nbv[0]
def qedi(mkepe, ytw, nbv):
     return (mkepe[0] != ytw[-1]) and (mkepe[-1] != nbv[0])
hlwxkh = Factor("vkv", [DerivedLevel("vqhjwa", Transition(kwoas, [mkepe, ytw, nbv])), DerivedLevel("xphfj", Transition(vvx, [mkepe, ytw, nbv])),DerivedLevel("vjxgzr", Transition(qedi, [mkepe, ytw, nbv]))])
### EXPERIMENT
design=[mkepe,ytw,nbv,hlwxkh]
crossing=[hlwxkh]
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