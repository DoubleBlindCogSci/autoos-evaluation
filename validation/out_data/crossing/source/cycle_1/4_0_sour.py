from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### REGULAR FACTORS
hhl = Factor("hhl", ["kjorlx", "jdpo"])
uxzmw = Factor("uxzmw", ["fgmu", "mcbni"])
jbda = Factor("jbda", ["hfh", "ioo"])
rspui = Factor("rspui", ["ydh", "efenx"])
pcbhls = Factor("pcbhls", ["givo", "iejky"])
zij = Factor("zij", ["ncecmx", "wqeey"])
qku = Factor("qku", ["dbma", "hcmgac"])

### EXPERIMENT
design=[hhl,uxzmw,jbda,rspui,pcbhls,zij,qku]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_0_0.csv"))
nr_crossings=4
nr_factors=7
p_code_1 = 0
p_code_2 = 0
crossing = [hhl]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [uxzmw,jbda,rspui,pcbhls]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [zij]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [qku]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)