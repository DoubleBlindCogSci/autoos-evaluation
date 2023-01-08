from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JfmA=Factor('DGMf',['KFBYQRG$t(8Rt',':evlU^Da0n','fkMsUUrrVwnq','EYtgegWyFLEZC'])
dOD2=Factor('$BqTAtQZR',[Level("deuc_<b",3),"Qnm[)WPhY","CPvx",";Eskx"])
rMVGG=Factor("RJdhjTrR)",['vAONvJuQMfDD','KX%LpLfwX','tL10fRF|iM',"@Ey"])

### EXPERIMENT
design=[JfmA,dOD2,rMVGG]
crossing=[JfmA,dOD2,rMVGG]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_3_0_0.csv"))
nr_factors=3
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)