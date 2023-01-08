from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ewFu25=["9YgqDljcwqwl",'T)aOsnFZxEDmw',Level("c?Zadgj",9),'ufVWhgu:AoyNB',"Z_h"]
xh7BeJvmnD_=Factor('h(mgDey',ewFu25)
u2d2iN=Factor("Kh|",[Level('Zz9aSPy vcpErG',6),Level("U5go",9),'NcEzH[VNhmYptq','nU)MZuJk','xOHHoQGf'])

### EXPERIMENT
design=[xh7BeJvmnD_,u2d2iN]
crossing=[xh7BeJvmnD_,u2d2iN]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_1_0.csv"))
nr_factors=2
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)