from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hBWicSi = Factor("hBWicSi", ["y]dOBUod{qkhkr", "9TGDc5da", "N(kKY*U:", "2pI", ">pw^kAb", "OyFQ5BXPxWR}OU", "mktJukpff", "dzV2Yv6vXYZb", "hrS?qNpTXGd"])
SbuGtOQYEJgK_ = Factor("SbuGtOQYEJgK;", [Level("WZaHmyj6ecC ", 2), "fBABK", "QVSGKUrBygaZ", "kirYh#Q", "eYnxxwz", "t~bcWXZlgag@jo", "$TSJ", "Ub$UGBLd{ 6mdz", "XSJp"])
nPIsbOq_O = Factor("nPIsbOq*O", [Level("PNyJgfNDB0}&y", 1), Level("FE@buAQ4mEaPt", 2), "SuY", "rew{N4wA[COD", "ChevS#rZ^", "BuS;UDkFqtF", "bkyL", "O Pf"])
Uw_EoqJpRB = Factor("Uw$EoqJpRB", ["VG[k?gJ5k", "H_do", "ee~#)BL", "Fhixn", "F#PQt*a", "dmCrz&LeP[p", "3sKJTNOdg5", "QR|iyiWh ", "Uzzoo", ":xe!?zymf"])

design=[hBWicSi,SbuGtOQYEJgK_,nPIsbOq_O,Uw_EoqJpRB]
crossing=[hBWicSi,SbuGtOQYEJgK_,nPIsbOq_O,Uw_EoqJpRB]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_4_0"))

### END
