from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
rhlqtt = Factor("rhlqtt", ["spaqpf","eols", "gmjo"])
osd = Factor("osd", ["ljh","tmg", "cyiv"])
jaxz = Factor("jaxz", ["hou","try","qmtxtw", "xbkj"])
sjln = Factor("sjln", ["hmdy", "pndj"])

### EXPERIMENT
constraints=[ExactlyK(4,(rhlqtt,"gmjo"))]
design=[rhlqtt,osd,jaxz,sjln]
crossing=[osd,jaxz,sjln]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/1_0_0.csv"))
nr_constraints=1
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)