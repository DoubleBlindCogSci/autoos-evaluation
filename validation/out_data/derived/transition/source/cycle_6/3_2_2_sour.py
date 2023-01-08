from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vyl = Factor("vyl", ["nfji","ewcnwl","zhrtv","gevbzq","mutl","omuphx"])
lytpda = Factor("lytpda", ["hmeuy","uqjxcp","bgh","kiwcz","rzqhjz","ewmcgk","hxdqz","ygzcc"])
def jjond(vyl, lytpda):
     return "omuphx" == vyl[-1] and lytpda[0] != "uqjxcp"
def kwefzx(vyl, lytpda):
     return "omuphx" != vyl[-1] and lytpda[0] == "uqjxcp"
def emotn(vyl, lytpda):
     return (vyl[-1] != "omuphx") and (lytpda[0] != "uqjxcp")
nrc = DerivedLevel("zigcr", Transition(jjond, [vyl, lytpda]))
ffkul = DerivedLevel("ltkzxi", Transition(kwefzx, [vyl, lytpda]))
vombk = DerivedLevel("xinlkr", Transition(emotn, [vyl, lytpda]))
togld = Factor("jljwku", [nrc, ffkul, vombk])

### EXPERIMENT
design=[vyl,lytpda,togld]
crossing=[togld]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)