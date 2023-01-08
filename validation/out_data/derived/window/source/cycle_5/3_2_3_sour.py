from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zwin = Factor("zwin", ["gylpcf","zdd","tid","lipuj","aajchu","flbwb","bixk","asxya"])
tqxev = Factor("tqxev", ["hnabb","nenp","blvuz","tkvk","rdjog","yub"])
def hrvcr(zwin, tqxev):
     return zwin[0] == "tid" and not tqxev[-1] == "yub"
def merfpo(zwin, tqxev):
     return "tid" != zwin[0] and  tqxev[-1] == "yub"
def rpuwqi(zwin, tqxev):
     return (not zwin[0] == "tid") and (tqxev[-1] != "yub")
oegvyf = Factor("nwm", [DerivedLevel("fbnbrn", Window(hrvcr, [zwin, tqxev],2)), DerivedLevel("gex", Window(merfpo, [zwin, tqxev],2)),DerivedLevel("gliqlb", Window(rpuwqi, [zwin, tqxev],2))])
### EXPERIMENT
design=[zwin,tqxev,oegvyf]
crossing=[oegvyf]
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