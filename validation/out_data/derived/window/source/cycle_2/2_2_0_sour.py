from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
rdt = Factor("rdt", ["umt","dycmaw","eck","jgpw","ekax"])
ilf = Factor("ilf", ["kpc","dgvk","yzyqgn","szym","qhas","nbb","wxky"])
def rjar(rdt, ilf):
    return rdt[-1] != "jgpw" or ilf[-2] != "qhas"
def fndguy(rdt,ilf):
    return not rjar(rdt, ilf)
fra = DerivedLevel("lpvlp", Window(rjar, [rdt, ilf],3))
husir = DerivedLevel("uiqx", Window(fndguy, [rdt, ilf],3))
ctgwb = Factor("rqjuv", [fra, husir])

### EXPERIMENT
design=[rdt,ilf,ctgwb]
crossing=[ctgwb]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)