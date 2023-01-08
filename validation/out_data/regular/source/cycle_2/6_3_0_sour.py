from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zGcjWOQc=Factor('ijDRyQgxkUTaL',['TlK(U',Level('ILnBfN',4),'YlGhk{rRndt',"m#zU4$yXzyY","xP(Kgw",'nlSTn2ltc^dA'])
BYo7gq=['BYHad',Level("eZErkqwuL!YuN",5),"CKoQWoaOG%o",'aDZ?kDGeN',Level("rm%JLscdRtCRnE",8),'dhOovPDTq3F&Ow',"T5jo*O","glXVl"]
MPeJiH0zPb=Factor("fCdWJg[agY4t",['X^y',"SsGnoU",Level('HuylBEsNI',3),BYo7gq[3],'4rK','Rs5HmgAl%1ze','sZlUeBAUd4B'])
bXFbI9ooI=Factor("bby<IGB",["VuhAlkZJuMGo",Level("M_vZsRG",2),"XTyslcxc4;DvGU",'sG*iqB',Level('dni{DyCPDp',2),'GnXo'])

### EXPERIMENT
design=[zGcjWOQc,MPeJiH0zPb,bXFbI9ooI]
crossing=[zGcjWOQc,MPeJiH0zPb,bXFbI9ooI]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_3_0_0.csv"))
nr_factors=3
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)