from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
s2vI8jH="vjztDnPOVQ"
E37FvSV=["c$UXoo*T#a4Tga",s2vI8jH,Level("Ciloc8EVVuQ",5),"WugJXtjPNS(H|","BqytigifTcHKZ",'FLtKVDyYx!rWP',Level('LSYzJkWhApAUAS',3),'nDh','Nt3foqW<f8',Level("fe@",2)]
lnWSD=Factor('Lsg}xEZvgVMQ1',E37FvSV)
EPC6hUqKMX='%fPqzLOKj'
pHAr=Factor("TQ3TAGfnnpom>W",['pOMWBcXP',"jDYptVHvnXUN",Level('5pgaMDHr',4),'cNNlBC;Mb',"HOE%M8jwLg","omPrKhjCjNSbF","HM[qt3IwiNtJX",EPC6hUqKMX,"dNajDwY#O;Tb(B",'ul0KMA'])

### EXPERIMENT
design=[lnWSD,pHAr]
crossing=[lnWSD,pHAr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/9_2_1_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/9_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)