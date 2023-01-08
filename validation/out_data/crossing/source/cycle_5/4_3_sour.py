from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pkb = Factor("pkb", ["jpmi", "ubt"])
zgn = Factor("zgn", ["dhekd", "nzep"])
frmuqy = Factor("frmuqy", ["xpxi", "uoqpv"])
ykfn = Factor("ykfn", ["pow", "ribpv"])
gxj = Factor("gxj", ["wzpgst", "yfr"])
qdsoe = Factor("qdsoe", ["vucd", "yrkpxf"])
pdh = Factor("pdh", ["dkmj", "sruuto"])
iiclld = Factor("iiclld", ["ghdr", "cxa"])
aeet = Factor("aeet", ["akf", "qeb"])
ybii = Factor("ybii", ["zrint", "prxho"])
czhfw = Factor("czhfw", ["lmxd", "dzr"])
mca = Factor("mca", ["emg", "udtnj"])

### EXPERIMENT
design=[pkb,zgn,frmuqy,ykfn,gxj,qdsoe,pdh,iiclld,aeet,ybii,czhfw,mca]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_0.csv"))
nr_crossings=4
nr_factors=12
p_code_1 = 0
p_code_2 = 0
crossing = [pkb,zgn,frmuqy]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ykfn,gxj,qdsoe,pdh]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [iiclld,aeet,ybii,czhfw]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [mca]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
