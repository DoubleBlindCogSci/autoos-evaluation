from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wej = Factor("wej", ["bevf", "eaklvp"])
buxe = Factor("buxe", ["jdj", "vqqf"])
aqzlz = Factor("aqzlz", ["wtwz", "fqlis"])
ucag = Factor("ucag", ["wff", "dsudg"])
zwnt = Factor("zwnt", ["uljiaw", "mfz"])
vvgt = Factor("vvgt", ["hvvh", "oyyby"])
jldenz = Factor("jldenz", ["jvi", "oniker"])
fzox = Factor("fzox", ["nyo", "ghbz"])
kptit = Factor("kptit", ["jmsy", "qnh"])

### EXPERIMENT
design=[wej,buxe,aqzlz,ucag,zwnt,vvgt,jldenz,fzox,kptit]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_6_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_6_0.csv"))
nr_crossings=3
nr_factors=9
p_code_1 = 0
p_code_2 = 0
crossing = [wej,buxe,aqzlz,ucag]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zwnt]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [vvgt,jldenz,fzox,kptit]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
