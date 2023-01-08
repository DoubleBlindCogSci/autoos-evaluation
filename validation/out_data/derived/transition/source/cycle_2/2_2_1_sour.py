from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ppo = Factor("ppo", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
vjsf = Factor("vjsf", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
utvdc = Factor("utvdc", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
def lkianh(ppo, utvdc, vjsf):
    return ppo[0] != utvdc[-1] and ppo[-1] == vjsf[0]
def groddj(ppo, utvdc, vjsf):
    return not lkianh(ppo, utvdc, vjsf)
oli = DerivedLevel("szx", Transition(lkianh, [ppo, vjsf, utvdc]))
swzbr = DerivedLevel("dvcood", Transition(groddj, [ppo, vjsf, utvdc]))
elvuso = Factor("paqaim", [oli, swzbr])

### EXPERIMENT
design=[ppo,vjsf,utvdc,elvuso]
crossing=[elvuso]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)