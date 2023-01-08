from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pjnbo = Factor("pjnbo", ["nlcks", "mtq"])
hte = Factor("hte", ["harjg", "izaae"])
kjeta = Factor("kjeta", ["bazf", "oeg"])
yqp = Factor("yqp", ["ggmwfy", "oloni"])
tsl = Factor("tsl", ["ubsx", "wpfgfv"])
pbis = Factor("pbis", ["wosbek", "ziwy"])
tzmhx = Factor("tzmhx", ["qnxkxp", "ntjpn"])
rfc = Factor("rfc", ["aob", "nyw"])
zmukm = Factor("zmukm", ["oey", "nle"])

### EXPERIMENT
design=[pjnbo,hte,kjeta,yqp,tsl,pbis,tzmhx,rfc,zmukm]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_0_0.csv"))
nr_crossings=4
nr_factors=9
p_code_1 = 0
p_code_2 = 0
crossing = [pjnbo]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [hte,kjeta,yqp]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [tsl,pbis,tzmhx]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [rfc,zmukm]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
