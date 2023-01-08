from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bzz = Factor("bzz", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
wuan = Factor("wuan", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
tbbie = Factor("tbbie", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
def qseewp(bzz, wuan, tbbie):
     return bzz[0] == wuan[-1] and bzz[-1] != tbbie[0]
def iauil(bzz, wuan, tbbie):
     return wuan[-1] != bzz[0] and bzz[-1] == tbbie[0]
def qzls(bzz, wuan, tbbie):
     return (not qseewp(bzz, wuan, tbbie)) and (bzz[-1] != tbbie[0])
xsg = DerivedLevel("kavhih", Transition(qseewp, [bzz, wuan, tbbie]))
lfz = DerivedLevel("ytt", Transition(iauil, [bzz, wuan, tbbie]))
rnpouz = DerivedLevel("wcaqvo", Transition(qzls, [bzz, wuan, tbbie]))
llrmt = Factor("mbgo", [xsg, lfz, rnpouz])

### EXPERIMENT
design=[bzz,wuan,tbbie,llrmt]
crossing=[llrmt]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)