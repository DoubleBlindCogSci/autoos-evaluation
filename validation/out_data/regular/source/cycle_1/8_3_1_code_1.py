from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GzZjFHmeA8=["qCi~_UREBIb",'6|yfeAo6R8Wj$',Level("byvZcF",2),Level("owY[k",2)]
STJ8B7FLG=['isChMWrYBGRde',"_JJjeUFGh",'EtyrG',GzZjFHmeA8[2],"aOyxW3|Vk:KB","w0u~W",'wTiefnWsm5UKK','WIgx*z4vES[BZM','JX%XvKFP $iSyp']
fZtmX7=Factor("OKJR!bFabtyQS",STJ8B7FLG)
IgmMoNNh=Level("g|tVwTfar",5)
D3vnwRJKtn7=Factor('NUGLwlghiUjUu',[Level("KZiVI",7),Level('yu:y5',4),"pOvSReyP5D","eHIUUWVw",IgmMoNNh,Level('u K',3),Level('ImCT',9),Level("ct9XyA",7),'RTdQdky'])
IVrOmso=["tdc",Level('Jgu',8),Level('NdStEO::}qAYo',4),'XO12KQDACTWFC',":Vt",Level("mnPru",8),'hIiVtGGQK7Ag',Level("Wvx!nW",4)]
BIdrtV4=Factor('gRMzN',IVrOmso)

### EXPERIMENT
design=[fZtmX7,D3vnwRJKtn7,BIdrtV4]
crossing=[fZtmX7,D3vnwRJKtn7,BIdrtV4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/8_3_1"))
### END