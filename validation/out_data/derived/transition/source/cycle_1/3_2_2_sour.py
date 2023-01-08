from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
duxbo = Factor("duxbo", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
cbrnt = Factor("cbrnt", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
rep = Factor("rep", ["wapejn","ebkaom","eiucr","eotvld","hinvt","hjgvt","xcty"])
def orgfgw(duxbo, cbrnt, rep):
     return cbrnt[-1] == duxbo[0]
def iqjn(duxbo, cbrnt, rep):
     return cbrnt[-1] != duxbo[0] and rep[0] == duxbo[-1]
def llt(duxbo, cbrnt, rep):
     return (not duxbo[0] == cbrnt[-1]) and (not iqjn(duxbo, cbrnt, rep))
ubfyl = Factor("nxqa", [DerivedLevel("xbata", Transition(orgfgw, [duxbo, cbrnt, rep])), DerivedLevel("qzxb", Transition(iqjn, [duxbo, cbrnt, rep])),DerivedLevel("bfl", Transition(llt, [duxbo, cbrnt, rep]))])
### EXPERIMENT
design=[duxbo,cbrnt,rep,ubfyl]
crossing=[ubfyl]
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