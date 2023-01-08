from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ljajs = Factor("ljajs", ["igja","pmshy","mmqrcq","njjjc","qhhlhv","kgzz","mgg"])
duebpi = Factor("duebpi", ["xvic","dpbx","nxfgd","sgo","gqrrqf","dph","yjo"])
def lsn(ljajs, duebpi):
     return ljajs[-1] == "mgg" and duebpi[0] != "dpbx"
def rvpsbb(ljajs, duebpi):
     return ljajs[-1] != "mgg" and duebpi[0] == "dpbx"
def qgnnap(ljajs, duebpi):
     return (not lsn(ljajs, duebpi)) and (not rvpsbb(ljajs, duebpi))
tbn = Factor("pnlg", [DerivedLevel("vpbr", Transition(lsn, [ljajs, duebpi])), DerivedLevel("kwcroh", Transition(rvpsbb, [ljajs, duebpi])),DerivedLevel("gtkpx", Transition(qgnnap, [ljajs, duebpi]))])
### EXPERIMENT
design=[ljajs,duebpi,tbn]
crossing=[tbn]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)