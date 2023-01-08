from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ysJFTNQaiMP=Factor('qcAJmQDvCchZy',["oBb?PyBrQwz","YzVWSjq6LBaQ","FwqmKR6UlJ","YDFmv",'Cvzw F$[N^',">nRhVopm:V",'TCwsYOzc',"1bubPsYDrU","gC}zo("])
csMYxj=["Eho3Pc","fuHMjSx",'46:*JDvXtK',"jx__z$RlCJH{w",'Jxxd<abHW','JnB(8p']
NOdWdpG=Factor('w3biplTVb*3',['EnQLTyc1cIhZVR',"Gmw6NG]tuy",Level('AnHg8p;_ETEvI',3),"Q%jhzDfi",'dvFS FysnTvssH',csMYxj[1],Level("vqmam84?ywV",1),'Inkdkmy','C<Q&SVzkz','D[KG&E)$'])
it03uPXANH="AwKEEXQ"
InYXEu2ua=['GAaYNeC',"2BXkeLAoGbtxr!",'sVYs}',"HVw","AILkGi7TBMOn>L","{bQHUc]y","agN zv VPuTVQC",it03uPXANH,'FBaELRELNScp','SBc']
C34SCiRU=Factor("BAdA&N",InYXEu2ua)

### EXPERIMENT
design=[ysJFTNQaiMP,NOdWdpG,C34SCiRU]
crossing=[ysJFTNQaiMP,NOdWdpG,C34SCiRU]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_3_1_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)