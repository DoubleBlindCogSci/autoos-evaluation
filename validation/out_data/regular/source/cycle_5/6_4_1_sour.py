from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eyA9cesK=Factor('yoaFxqvtb',["k8NeS",'xYTLCkuFMA(x',Level("WaPjr",1),"5ELMv^ujl^XfnQ",'mast_Q','xpAigKIpHcu'])
ESh4DLp=Factor("4ctPvTkxcwR@}Y",["L ggETb$r","XoX","iT07x",Level('n?hZi',3),Level('qfDj',1),'<jilf'])
qjVvlAWL=Factor('nvfwNpK_OB',['ZhHc|Oj%PhJxBW',"jr!MvOg",'cYGIHs',"m?X~BKgzYe",'AdzrNrKDD?5',"5W4SA"])
u6z_LnDaAH='r&sZ'
rruuo4=Factor("OA[aBte4c",['hLpIlIUs!ICYP',Level('aBrUguFn',3),'{iub',";PFkI#n2","YjP[CZyBpV4sX",'|f?',u6z_LnDaAH])

### EXPERIMENT
design=[eyA9cesK,ESh4DLp,qjVvlAWL,rruuo4]
crossing=[eyA9cesK,ESh4DLp,qjVvlAWL,rruuo4]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_4_1_0.csv"))
nr_factors=4
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)