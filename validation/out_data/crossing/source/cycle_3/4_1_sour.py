from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qha = Factor("qha", ["wdq", "iqa"])
jbu = Factor("jbu", ["mqs", "rser"])
psj = Factor("psj", ["gno", "omln"])
fod = Factor("fod", ["jpzc", "kias"])
ledros = Factor("ledros", ["uknau", "byf"])
fcs = Factor("fcs", ["nnczm", "diq"])
cftisd = Factor("cftisd", ["sbidgy", "wpkghw"])
dmeeb = Factor("dmeeb", ["vyg", "wulrex"])
tmb = Factor("tmb", ["vetd", "mvnk"])
alsj = Factor("alsj", ["tbb", "soktwa"])
aew = Factor("aew", ["mvz", "ful"])
xlo = Factor("xlo", ["mwib", "dnvhyb"])
vytrfn = Factor("vytrfn", ["mqmor", "otyoje"])
bne = Factor("bne", ["zyqcat", "nuhrml"])

### EXPERIMENT
design=[qha,jbu,psj,fod,ledros,fcs,cftisd,dmeeb,tmb,alsj,aew,xlo,vytrfn,bne]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_1_0.csv"))
nr_crossings=4
nr_factors=14
p_code_1 = 0
p_code_2 = 0
crossing = [qha,jbu,psj]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [fod,ledros,fcs]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [cftisd,dmeeb,tmb,alsj]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [aew,xlo,vytrfn,bne]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
