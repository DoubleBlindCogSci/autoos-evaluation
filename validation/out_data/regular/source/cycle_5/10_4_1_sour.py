from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tILb='x[smAoI'
uXcUMIe=Factor('GuZ',["VVw]bS uS","aYXjW","K?7Hma","p$XMTXmMCuqR","h^W1wMwgTR",'cIqL&DVvgivi','nObBwMQPshbddM',"CcQFxAzvaHwge2",'nJDK',"NBWAeK5mJEQxk",tILb])
jxLhW71="FcBv"
DdF5nFjn=["hnHaZhI",'~fG gQtCtP',"ag[avld","D;)kN8","Umm","VYLknJ7{",jxLhW71,"XdlXgRrQ","C]jf","DzThKA",'VqeAVfEaH7hU<']
zQm6wC4A=Factor("MMmje",DdF5nFjn)
xdojct=["sEPbM{~eFkN","SFm]YB",'uXbDVOyYs','nBWKZyw',"KRoX(hUdt","qdcjMxdsXMaMi",'EiTSrlo','VOQf_',"lVmOr%",Level('R%QIDbOo}zijyF',4)]
FtOxT=Factor('b%W2S#bFAH[ZE',xdojct)
BszKGFBR="lpskRS*j"
ZYqO6Mt115A=Factor("zT}ZvdN",['IiWQ@:k#YKBtDW','y9YvshhEdRh>Si','RkJ7&phvszYa',"NlyB3F",BszKGFBR,'pe1IfHTBwZF','jMfwkZpv',"FihNc#XOByT","TDxq<vK5ew$CK","ENs2dF",'AjHpzIRuc'])

### EXPERIMENT
design=[uXcUMIe,zQm6wC4A,FtOxT,ZYqO6Mt115A]
crossing=[uXcUMIe,zQm6wC4A,FtOxT,ZYqO6Mt115A]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/10_4_1_0.csv"))
nr_factors=4
nr_levels=10
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/10_4_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)