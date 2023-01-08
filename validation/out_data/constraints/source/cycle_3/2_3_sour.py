from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vqsru = Factor("vqsru", ["ssgt","wtd", "kdz"])
szji = Factor("szji", ["odysml", "tpt"])
fkuqb = Factor("fkuqb", ["vujh","drmoi", "eecyv"])
bpzkjs = Factor("bpzkjs", ["bub","qvib", "yfi"])
lwaowf = Factor("lwaowf", ["svertx","ggncdo","piwo", "nnnnsy"])

### EXPERIMENT
constraints=[AtLeastKInARow(2,(vqsru,"kdz")),AtMostKInARow(2,(szji,"tpt"))]
design=[vqsru,szji,fkuqb,bpzkjs,lwaowf]
crossing=[fkuqb,bpzkjs,lwaowf]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_3_0.csv"))
nr_constraints=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)