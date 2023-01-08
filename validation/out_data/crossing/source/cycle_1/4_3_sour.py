from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
iemv = Factor("iemv", ["isij", "qoooek"])
fum = Factor("fum", ["zgxqg", "erbdje"])
wclgu = Factor("wclgu", ["tgft", "vwkac"])
kdidwf = Factor("kdidwf", ["mfkw", "invtsc"])
pdodv = Factor("pdodv", ["bkgwzs", "avb"])
tgz = Factor("tgz", ["bqs", "bsa"])
cdwpvu = Factor("cdwpvu", ["twuje", "jgckv"])
ordv = Factor("ordv", ["hzca", "efwiof"])
lwe = Factor("lwe", ["vui", "klsqys"])
ufkn = Factor("ufkn", ["ovm", "xnqmvq"])
lqfm = Factor("lqfm", ["taotot", "jkjtj"])
acx = Factor("acx", ["ynupos", "kyl"])
sswl = Factor("sswl", ["fqvfl", "chmr"])
blt = Factor("blt", ["ndzbe", "eviqaw"])

### EXPERIMENT
design=[iemv,fum,wclgu,kdidwf,pdodv,tgz,cdwpvu,ordv,lwe,ufkn,lqfm,acx,sswl,blt]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_0.csv"))
nr_crossings=4
nr_factors=14
p_code_1 = 0
p_code_2 = 0
crossing = [iemv,fum,wclgu]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [kdidwf,pdodv,tgz]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [cdwpvu,ordv,lwe,ufkn]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [lqfm,acx,sswl,blt]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
