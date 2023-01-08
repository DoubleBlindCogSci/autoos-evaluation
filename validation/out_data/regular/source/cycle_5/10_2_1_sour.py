from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KEZbuPu=Factor('OGhyxfKA',['CyJRwFTVSTXbZ',"5>OvauYdNTy",'GIAsZeoe)UW_',"uUkEpboE",Level('GpIF oIPiLs',3),'xEhxor_hDDM1xm',"3Ym",'@rcBr',"P{ DbDpbFxUHeX","qPGg_suDXp)Dy!"])
u2fIvWG91c='XwKBLaBs'
Ut6DzC6z='bJYzMGO'
kufr2o=["WGdrC4R","~HiSlNh",'uZoH',":POtdtAsg>J",Ut6DzC6z,"O390dJsFo",'A4co9Eba(wS:{',"jmG",'lcD','kCMfMrs',u2fIvWG91c,'Xp0)iqc']
JBEi_feiwg=Factor('EEoQq',kufr2o)

### EXPERIMENT
design=[KEZbuPu,JBEi_feiwg]
crossing=[KEZbuPu,JBEi_feiwg]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/10_2_1_0.csv"))
nr_factors=2
nr_levels=10
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/10_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)