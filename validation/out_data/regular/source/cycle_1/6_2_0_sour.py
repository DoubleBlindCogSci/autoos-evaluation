from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
O7wieF=Factor('jUf;GSNjsdU<E?',['wsnZnqLWlD','a$tmZO',"EL(zDtnWikAAw","TMm5ZB",'CzhjVwxjc1?cbV',Level('rPfCErTNe',3)])
ljl8Kseo0=[']^F',"8bdJ",'w_e};^C@NPhWM',Level('TnOQoUDtN',5),']QCdmJ',';gMlwG']
tPvnBVZuD0U=Factor("BRpwg n",ljl8Kseo0)

### EXPERIMENT
design=[O7wieF,tPvnBVZuD0U]
crossing=[O7wieF,tPvnBVZuD0U]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_2_0_0.csv"))
nr_factors=2
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)