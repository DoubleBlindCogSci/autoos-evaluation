from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
guy = Factor("guy", ["rtnabe","xpkjko","ctc","sdv","egjb","lhdxe","ztpvlx","kgm"])
ooagz = Factor("ooagz", ["cxkdhe","gbxv","jiyrm","kolng","tzyoei","iazcku","jll"])
def whkm(guy, ooagz):
     return "egjb" == guy[-1] and not ooagz[0] == "cxkdhe"
def mky(guy, ooagz):
     return guy[-1] != "egjb" and ooagz[0] == "cxkdhe"
def xseihr(guy, ooagz):
     return (not whkm(guy, ooagz)) and (not mky(guy, ooagz))
hsk = DerivedLevel("cmidw", Transition(whkm, [guy, ooagz]))
vvhnc = DerivedLevel("fncgbm", Transition(mky, [guy, ooagz]))
xlv = DerivedLevel("ila", Transition(xseihr, [guy, ooagz]))
qugixe = Factor("sjkko", [hsk, vvhnc, xlv])

### EXPERIMENT
design=[guy,ooagz,qugixe]
crossing=[qugixe]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)