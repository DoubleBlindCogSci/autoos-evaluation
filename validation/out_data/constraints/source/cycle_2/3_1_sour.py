from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ghgsgh = Factor("ghgsgh", ["ygygmn","bhhi","wswgl", "miilqs"])
jzbdqh = Factor("jzbdqh", ["tebltl","owcd", "ctucf"])
ajw = Factor("ajw", ["psmlbt", "ayhrhh"])
gqju = Factor("gqju", ["atn", "xdgug"])
qtjk = Factor("qtjk", ["omyo","kdh","euw", "vhuhb"])

### EXPERIMENT
constraints=[AtLeastKInARow(3,(ghgsgh,"miilqs")),AtMostKInARow(3,(jzbdqh,"ctucf")),ExactlyKInARow(3,(ajw,"ayhrhh"))]
design=[ghgsgh,jzbdqh,ajw,gqju,qtjk]
crossing=[gqju,qtjk]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0.csv"))
nr_constraints=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)