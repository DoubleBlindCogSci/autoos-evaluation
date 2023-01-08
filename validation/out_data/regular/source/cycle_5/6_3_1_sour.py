from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
f4Zws6JrXJ=["<LNtSV",'%ZHAtUoQD',"PrH",'te9nWzStC',"t!m{YqJd","zkWIHDEMn"]
HFb4KO2XOq=Factor(' KRGb]oxJ S%E',f4Zws6JrXJ)
bnGov5Z=['j#n#t',"QjgG_zuF",'vX[OaFdCWV','VEBlp','CSaQe#6CYihBGy']
JRwwyE4uKxz=[bnGov5Z[3],"Or5F1pdvJaT|Sk",'QtUWmc$Np|',"?U6MT","N)rIBZqwjGQ",'SiwZSDH(',"aah3EeA"]
sn0iAJH_2=Factor("Ncvzjt~zwtl",JRwwyE4uKxz)
QGS1=['eSfvQg',Level(" N} bG8IiO",2),Level("9n>",3),"2Y1JFWinNt5","SJjHwS$",'YKhkxIXGNeuzYM']
dLp5J6Bu3M=Factor('%OCBIdJXiSXz',QGS1)

### EXPERIMENT
design=[HFb4KO2XOq,sn0iAJH_2,dLp5J6Bu3M]
crossing=[HFb4KO2XOq,sn0iAJH_2,dLp5J6Bu3M]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_3_1_0.csv"))
nr_factors=3
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)