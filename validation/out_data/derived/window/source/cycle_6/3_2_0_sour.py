from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
egwrq = Factor("egwrq", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
sgrux = Factor("sgrux", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
vgzhs = Factor("vgzhs", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
def tupqc(egwrq, sgrux, vgzhs):
     return sgrux[0] == egwrq[-1] and egwrq[0] != vgzhs[-1]
def ngdnu(egwrq, sgrux, vgzhs):
     return sgrux[0] != egwrq[-1] and egwrq[0] == vgzhs[-1]
def toku(egwrq, sgrux, vgzhs):
     return (not egwrq[-1] == sgrux[0]) and (egwrq[0] != vgzhs[-1])
qrpuio = DerivedLevel("svi", Window(tupqc, [egwrq, sgrux, vgzhs],2))
tbxp = DerivedLevel("wkej", Window(ngdnu, [egwrq, sgrux, vgzhs],2))
ldf = DerivedLevel("sugtp", Window(toku, [egwrq, sgrux, vgzhs],2))
qhr = Factor("uheab", [qrpuio, tbxp, ldf])

### EXPERIMENT
design=[egwrq,sgrux,vgzhs,qhr]
crossing=[qhr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)