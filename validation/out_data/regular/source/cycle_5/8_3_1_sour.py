from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
XNDPvbMGi='cW{Ilk~y~POT'
thtynil6=['WZpwSCHq','ImrE]lduw{Qksl',"$e&Q",'PNeqBHUqsIG','Q<o',XNDPvbMGi,'lH;EzXs',Level('nnIiGKcue',3),'vXOuPJKKz']
hT362k=Factor('cqM',thtynil6)
UyuPUlN4='i<vBBQxdFIr'
MUTWfc4l=Factor('cyANfIZJpQOgh$',[Level('?VIecNgjZ!>',2),'DRD',Level("epr@z:NXTgrVVw",3),'iZiVT','6#mpkRrIqrf',UyuPUlN4,"UnCC>jMoA","OqnmMYNff>U","eQ1|T{I^"])
v_GdC7U=["JHWoN",'rFMlkftlF','wG YzNeGxuJvE',"ID?se7vmMz",'SVJgykI',"5PrE?z jT",'Oh<DPIgw',"JBGdUQ8LX"]
ggbxk=Factor("Dkk{DvU^",v_GdC7U)

### EXPERIMENT
design=[hT362k,MUTWfc4l,ggbxk]
crossing=[hT362k,MUTWfc4l,ggbxk]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_3_1_0.csv"))
nr_factors=3
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)