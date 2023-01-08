from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jifmc = Factor("jifmc", ["njln","gzz","stnk","ylbkuh","bhr","sesr","gdupd","nxta"])
hasycl = Factor("hasycl", ["njln","gzz","stnk","ylbkuh","bhr","sesr","gdupd","nxta"])
cydh = Factor("cydh", ["njln","gzz","stnk","ylbkuh","bhr","sesr","gdupd","nxta"])
def oakuy(jifmc, hasycl, cydh):
     return hasycl[-1] == jifmc[0] and jifmc[-1] != cydh[0]
def hwthv(jifmc, hasycl, cydh):
     return hasycl[-1] != jifmc[0] and cydh[0] == jifmc[-1]
def bhus(jifmc, hasycl, cydh):
     return (jifmc[0] != hasycl[-1]) and (not hwthv(jifmc, hasycl, cydh))
tbeo = DerivedLevel("jieox", Window(oakuy, [jifmc, hasycl, cydh],2,1))
jbx = DerivedLevel("cnnrmc", Window(hwthv, [jifmc, hasycl, cydh],2,1))
ppqe = DerivedLevel("hfyt", Window(bhus, [jifmc, hasycl, cydh],2,1))
qpjya = Factor("yysx", [tbeo, jbx, ppqe])

### EXPERIMENT
design=[jifmc,hasycl,cydh,qpjya]
crossing=[qpjya]
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