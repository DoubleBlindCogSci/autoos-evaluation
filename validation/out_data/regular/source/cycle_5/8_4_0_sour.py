from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wxpx="hrS?qNpTXGd"
jzABin4_Fh4=Factor("hBWicSi",["y]dOBUod{qkhkr",'9TGDc5da',"N(kKY*U:",'2pI',">pw^kAb",'OyFQ5BXPxWR}OU',"mktJukpff",'dzV2Yv6vXYZb',wxpx])
xSX36q2ZmO=Level('WZaHmyj6ecC ',2)
IXgEN1Wi=[xSX36q2ZmO,"fBABK",'QVSGKUrBygaZ',"kirYh#Q",'eYnxxwz','t~bcWXZlgag@jo',"$TSJ","Ub$UGBLd{ 6mdz",'XSJp']
O49IQdUc=Factor('SbuGtOQYEJgK;',IXgEN1Wi)
fgqUw84D=['PNyJgfNDB0}&y',Level('FE@buAQ4mEaPt',1),'SuY','rew{N4wA[COD','ChevS#rZ^',"BuS;UDkFqtF",'bkyL','O Pf']
zC5NO=Factor("nPIsbOq*O",fgqUw84D)
q_IsRpOdv66='dmCrz&LeP[p'
vRMOlC8='F#PQt*a'
qYoYH=Factor('Uw$EoqJpRB',["VG[k?gJ5k",'H_do','ee~#)BL',"Fhixn",vRMOlC8,q_IsRpOdv66,"3sKJTNOdg5","QR|iyiWh ",'Uzzoo',':xe!?zymf'])

### EXPERIMENT
design=[jzABin4_Fh4,O49IQdUc,zC5NO,qYoYH]
crossing=[jzABin4_Fh4,O49IQdUc,zC5NO,qYoYH]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_4_0_0.csv"))
nr_factors=4
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_4_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)