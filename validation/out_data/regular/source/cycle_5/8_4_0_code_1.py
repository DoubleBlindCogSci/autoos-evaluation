from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_4_0"))
### END