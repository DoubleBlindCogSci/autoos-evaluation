from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
X1ee='klXGVleXh'
DGHM8aSU_Wq=Factor("RBo",['b$ZiSLoFmmg',X1ee,"OnwGa",Level('jOcz',7),'VsthfWm',Level("YQILxAcQYra",4),Level("$vqBxq",7)])
zBr61X=Level("m#eYvv<HIEwIN",3)
brcdIMF=['TyNGASA$Ryheot',Level("VFeDO%4:",4),"JiUgRKF",'fvDDe',"BQmvXeGpYvev*M",Level('GDGohhXiJe;',9),zBr61X]
kWGVK8yDjo=Factor('ZcOY',brcdIMF)
OdlKtz5jKH=Factor('nbgswoYdxzc?',[Level('6FnN HJhVlK',7),'lLwGRqHP',"paE;uW",Level("SNIarJ",7),'EbgG ',Level("wRx9kbOkRg",3)])

### EXPERIMENT
design=[DGHM8aSU_Wq,kWGVK8yDjo,OdlKtz5jKH]
crossing=[DGHM8aSU_Wq,kWGVK8yDjo,OdlKtz5jKH]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_3_1_0.csv"))
nr_factors=3
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)