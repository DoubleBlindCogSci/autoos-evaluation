from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yyaxty = Factor("yyaxty", ["vlni", "gic"])
tovgxc = Factor("tovgxc", ["uvqg", "wasrf"])
unbw = Factor("unbw", ["bnb", "llma"])
mdfbrh = Factor("mdfbrh", ["icennq", "kkkyp"])
nboknq = Factor("nboknq", ["kmvca", "dcg"])
usiemr = Factor("usiemr", ["pnztwr", "dgxxhf"])

### EXPERIMENT
design=[yyaxty,tovgxc,unbw,mdfbrh,nboknq,usiemr]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/4_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/4_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [unbw,mdfbrh,nboknq]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [usiemr]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [tovgxc]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [yyaxty]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 4
nr_factors = 6
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
