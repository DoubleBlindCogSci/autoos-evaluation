from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
viNOzS=Factor('jyMJFmejL^$riP',[Level('dJI%LKQM2b',8),"6nNM9JzBH",'4lvw9vkCXAd','b5v#{rQmbVl',Level("dnVGG$jGosiw",4),"CsLiKY","X3]Xg%Ybv(SS","sJEXiFaDEPF2tI",Level("uinKOa?R4NQ^p;",5)])
N7prew=["vaoA",Level("aZ!YBxSO",5),'{AVQE','LBYK_mIvsATdRY',"kDlxS_}VgRTK"]
b7YHa6W=Level("cmSrfDovTtUU",10)
AAKNpTg=Factor('b;xatqivt',['pC4]5quBFbYx#',"rRgLFs_b","Y&IqDNTxiZ",Level('ENeYshy',1),"CDwDwCV","FJ{H8",Level("MYmNwuFq",3),N7prew[3],b7YHa6W,'d:UQ','ghbnXlPeFaKhGL'])

### EXPERIMENT
design=[viNOzS,AAKNpTg]
crossing=[viNOzS,AAKNpTg]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_2_0_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)