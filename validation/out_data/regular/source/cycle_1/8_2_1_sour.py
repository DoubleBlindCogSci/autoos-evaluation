from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZDXzy6L1vSx=Level('ShtIhkGJAUZ>c',10)
fIxqkOPpIY=Factor("0D{b~bxWrwQ[",["cEG|AN",'AxYZHAuaw:KhLA',"#ynLG<LYipZUi","WWJYaXjVdZjk{","gT (ibn|nvV",ZDXzy6L1vSx,"YD EuFMgoO",'RWcR[gfEw','AzRHf'])
c6YMgchMqv=["YDbPSaXjqFd(",Level("iwx",6),"vOb2$Yfyz5","5aZM<","GQmm?Gq",Level('vRPsA)vO#7z',10),Level("!vT",1),'KM:klJAhW|h']
g9P7bBki=Factor("?^i",c6YMgchMqv)

### EXPERIMENT
design=[fIxqkOPpIY,g9P7bBki]
crossing=[fIxqkOPpIY,g9P7bBki]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/8_2_1_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/8_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)