from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
yrcneo = Factor("yrcneo", ["cvpjht","akn","fpuslh","mtkpab","pygjc"])
ixp = Factor("ixp", ["cuf","xuebm","zcio","ufdatp","zdwdp"])
def byjjot(yrcneo, ixp):
    return yrcneo[-3] != "mtkpab" and ixp[0] != "zcio"
def ezupnv(yrcneo,ixp):
    return yrcneo[-3] == "mtkpab" or ixp[0] == "zcio"
myyhpf = DerivedLevel("dlg", Window(byjjot, [yrcneo, ixp],4))
ckwqu = DerivedLevel("ooynm", Window(ezupnv, [yrcneo, ixp],4))
zrdgap = Factor("ykb", [myyhpf, ckwqu])

### EXPERIMENT
design=[yrcneo,ixp,zrdgap]
crossing=[zrdgap]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)