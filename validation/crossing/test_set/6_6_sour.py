from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bzayws = Factor("bzayws", ["qyhh", "mdwens"])
xhrfl = Factor("xhrfl", ["acg", "busj"])
aquf = Factor("aquf", ["zvf", "egco"])
xcw = Factor("xcw", ["wnplqq", "hgth"])
yta = Factor("yta", ["epf", "jwph"])
qqeazh = Factor("qqeazh", ["enba", "baer"])

### EXPERIMENT
design=[bzayws,xhrfl,aquf,xcw,yta,qqeazh]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_6_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_6_0.csv"))
nr_crossings = 1
nr_factors=6
p_code_1 = 0
p_code_2 = 0
crossing = bzayws
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = xhrfl
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = aquf
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = xcw
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = yta
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = qqeazh
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [bzayws,xhrfl,aquf,xcw,yta,qqeazh]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
