from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
MiP0=Level("cLx!hbAF",2)
oY5RsBK=Factor("nmCqS Q",[Level('bjLAX_e',10),Level("<AxMNV",3),MiP0,Level('Eify',3),'hdJNxVjQu%YMx',"NjGk","JjeVDq*T8sUxgb",Level("IDHq",5),Level('igjzQGT!!bqxO',7)])
GNhd=Factor('!MVb',["N[sLUNL",Level('uliPi>L{vYZu<',6),"D@KQ mM",'KcXYF9nJW','4EfGTqk[] M',"QjUXhkmxGl",'JvHTCWUAS&{',Level("Q aCECGmsOF0V",10)])
jpq6=['Jbfn','uj3N]t<dcgr',"Bd~Uhe(eHn",'WZw:NZj',Level('NyZQVF4JR|QWvw',3),Level('Lhe^Xnx',4),'JMeoz_WQO','7pbBGocj']
fkYd0rgS5=Factor("LMIBd{RN",jpq6)

### EXPERIMENT
design=[oY5RsBK,GNhd,fkYd0rgS5]
crossing=[oY5RsBK,GNhd,fkYd0rgS5]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/8_3_0_0.csv"))
nr_factors=3
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/8_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)