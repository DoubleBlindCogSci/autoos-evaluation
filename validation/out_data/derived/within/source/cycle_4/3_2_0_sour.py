from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
epjvsp = Factor("epjvsp", ["lub","ofc","cfuj","wkah","vlrfg","uzqq","kcbik"])
vfowp = Factor("vfowp", ["runks","rpaaj","gsat","ekm","gie","vty","jgzgd"])
def swhd(epjvsp, vfowp):
     return epjvsp == "vlrfg"
def grvnc(epjvsp, vfowp):
     return "vlrfg" != epjvsp and  vfowp == "gsat"
def yklzn(epjvsp, vfowp):
     return (not epjvsp == "vlrfg") and (not grvnc(epjvsp, vfowp))
syme = DerivedLevel("rcvuob", WithinTrial(swhd, [epjvsp, vfowp]))
ijtcan = DerivedLevel("ympx", WithinTrial(grvnc, [epjvsp, vfowp]))
egtj = DerivedLevel("vqro", WithinTrial(yklzn, [epjvsp, vfowp]))
qaodrv = Factor("zdao", [syme, ijtcan, egtj])

### EXPERIMENT
design=[epjvsp,vfowp,qaodrv]
crossing=[qaodrv]
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