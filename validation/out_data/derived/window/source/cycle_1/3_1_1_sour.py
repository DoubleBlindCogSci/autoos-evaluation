from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
qbxrsc = Factor("qbxrsc", ["zxari","onc","zsbmrx","lgga","mrs","tqt","qxfhwx","uqpib"])
def sopu(qbxrsc):
     return qbxrsc[-3] == "zsbmrx"
def qqcgi(qbxrsc):
     return qbxrsc[0] == "qxfhwx"
def iqj(qbxrsc):
     return (qbxrsc[-3] != "zsbmrx") and (qbxrsc[0] != "qxfhwx")
cxlu = Factor("jtk", [DerivedLevel("eabp", Window(sopu, [qbxrsc],4)), DerivedLevel("csw", Window(qqcgi, [qbxrsc],4)),DerivedLevel("zjiomh", Window(iqj, [qbxrsc],4))])
### EXPERIMENT
design=[qbxrsc,cxlu]
crossing=[cxlu]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)