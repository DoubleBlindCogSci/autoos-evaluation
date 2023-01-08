from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hisfv = Factor("hisfv", ["bji", "gwm"])
anw = Factor("anw", ["cxph", "burq"])
akm = Factor("akm", ["dqc", "fjaak"])
xvku = Factor("xvku", ["qrmqm", "hemcr"])
hqte = Factor("hqte", ["voqekg", "eqmhpg"])
qqeqce = Factor("qqeqce", ["thux", "rlqczm"])
yqwa = Factor("yqwa", ["irfol", "ixxd"])
rxt = Factor("rxt", ["xsimsv", "jbo"])
usigz = Factor("usigz", ["xtvj", "vmiwdy"])
efudzv = Factor("efudzv", ["knf", "kztk"])
jhqq = Factor("jhqq", ["qxt", "cohbby"])
llpseo = Factor("llpseo", ["yzm", "vtxsd"])
dxr = Factor("dxr", ["ltrc", "gbvyf"])
hln = Factor("hln", ["ixohgn", "awirbk"])
jauytr = Factor("jauytr", ["plab", "kije"])

### EXPERIMENT
design=[hisfv,anw,akm,xvku,hqte,qqeqce,yqwa,rxt,usigz,efudzv,jhqq,llpseo,dxr,hln,jauytr]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/5_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/5_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [rxt,usigz,efudzv,jhqq]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [xvku,hqte,qqeqce,yqwa]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [llpseo,dxr,hln]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [hisfv,anw,akm]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [jauytr]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 5
nr_factors = 15
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
