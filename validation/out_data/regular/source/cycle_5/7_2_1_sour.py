from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
g94nw82jbB=Level("{haV",2)
VBa5lm=Factor("YE<",["YBZJBxV","PDS","WJHuH|rDXHnHUe","hgdgZyj","UJZ",'Rue',g94nw82jbB,"exaZ"])
OrjRR08GwD=Factor("BTKTWe@kyCgvN",["}pY",'XoLR',"rvsjPXCGcnqdgg",Level("eFNXMVmtGQYl",4),"qzLkbpGUUwd",'^efYWfnP',"ssmIXo"])

### EXPERIMENT
design=[VBa5lm,OrjRR08GwD]
crossing=[VBa5lm,OrjRR08GwD]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_2_1_0.csv"))
nr_factors=2
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)