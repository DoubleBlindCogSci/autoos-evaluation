from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
cridpl = Factor("cridpl", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
fra = Factor("fra", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
sqhrna = Factor("sqhrna", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
def yswa(cridpl, fra, sqhrna):
     return fra[-1] == cridpl[0]
def bpic(cridpl, fra, sqhrna):
     return fra[-1] != cridpl[0] and cridpl[-1] == sqhrna[0]
def mio(cridpl, fra, sqhrna):
     return (not yswa(cridpl, fra, sqhrna)) and (not cridpl[-1] == sqhrna[0])
mef = DerivedLevel("vek", Transition(yswa, [cridpl, fra, sqhrna]))
gsfyq = DerivedLevel("nfgszz", Transition(bpic, [cridpl, fra, sqhrna]))
gwuaez = DerivedLevel("fckuoh", Transition(mio, [cridpl, fra, sqhrna]))
dgej = Factor("wjjh", [mef, gsfyq, gwuaez])

### EXPERIMENT
design=[cridpl,fra,sqhrna,dgej]
crossing=[dgej]
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