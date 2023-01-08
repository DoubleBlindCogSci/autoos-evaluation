from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gMyTf=Factor('_HAzv',["gr&GSlM",'9xdOnDHGXf','UNOTTFk)AFMq0',"U1*mng J","BZysJvDInew",'FSHhEAThvq4','{{BS',"FtPqFz","AdpSV|TDjYLoN"])
qykWnECF=Factor("RabtMGmqX",[Level("ZgGspLf nfkGor",9),"*FChWzjw",'L}d',"QhJJMKxIbjFcEk",Level('uWf;kYbym#JIk',4),'CGC',"Mvd",Level('kMHQP',3),Level("{u3K EaIG",3)])
PPgDXh=Factor("LFsvlDVeGo$",["DSVIcFpZBQZ","utGw",Level("EZWxy>hD6h",3),'uzZQFDKw]WIe','OxkwKnHt?','rW>S&p','Y1TaFMKq tRA','bDJVif',Level('G7~sZf VBE$r',5)])

### EXPERIMENT
design=[gMyTf,qykWnECF,PPgDXh]
crossing=[gMyTf,qykWnECF,PPgDXh]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/9_3_0_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/9_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)