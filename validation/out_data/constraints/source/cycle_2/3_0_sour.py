from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jvrw = Factor("jvrw", ["zlebup","jgos", "pbzw"])
ipj = Factor("ipj", ["mrwhgp","vnbza","umgq", "tvibc"])
dqgb = Factor("dqgb", ["qjmic","lvfk", "awada"])
qdyr = Factor("qdyr", ["gkoqk","pmz", "norf"])
rnaqv = Factor("rnaqv", ["xeyirg","qivre","hrof", "soa"])
lit = Factor("lit", ["pvlfwy","idjr", "ihjkd"])

### EXPERIMENT
constraints=[MinimumTrials(47),ExactlyKInARow(2,(ipj,"tvibc")),Exclude(dqgb,"awada")]
design=[jvrw,ipj,dqgb,qdyr,rnaqv,lit]
crossing=[qdyr,rnaqv,lit]
### APPENDIX
block=Block(design,crossing,constraints)
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_0_0.csv"))
nr_constraints=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["constraints"], test_code_2["constraints"], nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)