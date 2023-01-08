from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jmhfj = Factor("jmhfj", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
insqbc = Factor("insqbc", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
rrf = Factor("rrf", ["sqn","prntw","griwh","qldgod","miaihz","dmoxo","kra","eiypb"])
def ftmayx(jmhfj, rrf, insqbc):
     return jmhfj == rrf
def oofkb(jmhfj, rrf, insqbc):
     return rrf != jmhfj and jmhfj == insqbc
def ixmvkr(jmhfj, rrf, insqbc):
     return (jmhfj != rrf) and (jmhfj != insqbc)
qwefo = DerivedLevel("pltfpx", WithinTrial(ftmayx, [jmhfj, insqbc, rrf]))
fnv = DerivedLevel("mkb", WithinTrial(oofkb, [jmhfj, insqbc, rrf]))
pampmw = DerivedLevel("ppugl", WithinTrial(ixmvkr, [jmhfj, insqbc, rrf]))
azoirk = Factor("awwa", [qwefo, fnv, pampmw])

### EXPERIMENT
design=[jmhfj,insqbc,rrf,azoirk]
crossing=[azoirk]
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