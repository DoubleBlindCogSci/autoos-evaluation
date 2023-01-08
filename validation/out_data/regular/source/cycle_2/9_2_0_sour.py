from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NuKCQfoe=Level("KRsuNgOkEA",8)
bkTn_ivYsWl=Factor('VXgn',[Level("pFuROZI",10),'AL:Rm',Level('H%ezN>9cIA8Z',10),Level("C4dy",5),"KAEiGsZv!gDEqx",NuKCQfoe,'h<XqmUzks ko',Level("qD7",9),"gZSo",Level('AIJTUuUnYi#7q',10)])
Yeap7=Factor("gzlpiy",[Level('sNRD^CUTY',2),'PyDkyB5H(x@',Level('AlW',2),"p tewt",'AS@MZGGvJDCgs','pw!',Level('F#igtIMhgbzrwi',1),Level("gjn:S",9),"vb_EeQVca]j"])

### EXPERIMENT
design=[bkTn_ivYsWl,Yeap7]
crossing=[bkTn_ivYsWl,Yeap7]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_2_0_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)