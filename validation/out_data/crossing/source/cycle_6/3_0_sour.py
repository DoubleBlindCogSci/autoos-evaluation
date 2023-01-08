from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kefhtd = Factor("kefhtd", ["guhest", "tjdvjg"])
anrzeu = Factor("anrzeu", ["dfwb", "ppxfb"])
flv = Factor("flv", ["mlrnh", "iioq"])
eoqu = Factor("eoqu", ["rvrtvg", "zxmpu"])
gafnq = Factor("gafnq", ["uyed", "iaorrb"])
tsasmd = Factor("tsasmd", ["uqkrvc", "mgl"])
eabf = Factor("eabf", ["octxf", "gyjk"])

### EXPERIMENT
design=[kefhtd,anrzeu,flv,eoqu,gafnq,tsasmd,eabf]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/3_0_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/3_0_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [kefhtd,anrzeu,flv]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [tsasmd,eabf]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [eoqu,gafnq]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
nr_crossings = 3
nr_factors = 7
df = pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
