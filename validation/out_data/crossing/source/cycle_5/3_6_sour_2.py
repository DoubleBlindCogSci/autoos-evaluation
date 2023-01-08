from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
wej = Factor("wej", ["bevf", "eaklvp"])
buxe = Factor("buxe", ["jdj", "vqqf"])
aqzlz = Factor("aqzlz", ["wtwz", "fqlis"])
ucag = Factor("ucag", ["wff", "dsudg"])
zwnt = Factor("zwnt", ["uljiaw", "mfz"])
vvgt = Factor("vvgt", ["hvvh", "oyyby"])
jldenz = Factor("jldenz", ["jvi", "oniker"])
fzox = Factor("fzox", ["nyo", "ghbz"])
kptit = Factor("kptit", ["jmsy", "qnh"])
constraints = []
crossing = [[wej, buxe, aqzlz, ucag], [zwnt, vvgt, jldenz, fzox, kptit]]


design=[wej,buxe,aqzlz,ucag,zwnt,vvgt,jldenz,fzox,kptit]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_6_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_6_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [wej, buxe, aqzlz, ucag]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ zwnt, vvgt, jldenz, fzox, kptit]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
