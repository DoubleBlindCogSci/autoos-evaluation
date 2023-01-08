from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zsgb = Factor("zsgb", ["rwwo", "cacbck"])
slpkqw = Factor("slpkqw", ["sxbhy", "ahxg"])
ykb = Factor("ykb", ["oon", "elz"])
uizcuo = Factor("uizcuo", ["roppm", "hrxz"])
xtffon = Factor("xtffon", ["lij", "thxld"])
tzhx = Factor("tzhx", ["hng", "uikcof"])
tzypp = Factor("tzypp", ["dcdyuq", "dsc"])
zgrei = Factor("zgrei", ["gaffl", "pcqs"])
iurc = Factor("iurc", ["kwrr", "qmisd"])
mbwxg = Factor("mbwxg", ["wigm", "bvw"])
ziyw = Factor("ziyw", ["fwk", "myiqf"])
sqlj = Factor("sqlj", ["kscwp", "kqayzs"])
yavu = Factor("yavu", ["yfl", "scayz"])

### EXPERIMENT
design=[zsgb,slpkqw,ykb,uizcuo,xtffon,tzhx,tzypp,zgrei,iurc,mbwxg,ziyw,sqlj,yavu]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [tzypp,zgrei,iurc,mbwxg]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ykb,uizcuo,xtffon,tzhx]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ziyw,sqlj,yavu]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zsgb,slpkqw]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 4
nr_factors = 13
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
