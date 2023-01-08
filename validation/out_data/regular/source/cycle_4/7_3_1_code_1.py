from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NK3Rb3lw0='5mJmPVI'
JJA8TFHo=[Level("upXMuXEIj>t^",2),"QTggMR",'WEEY%CoE','$tkA',"NQi",Level('BIBZv',4),'ZAUExL(',"bS1FNxDg"]
a4mF8=Factor("ydAaf6#dCAAz",["dLwZ(YH",JJA8TFHo[3],"j#7wTVQ","OHh",NK3Rb3lw0,'YSsn;oH',')lU)tFtt',"2Fgxhis%","t2Wd"])
AryDl2eChY7=Factor("et#V",['GSxn}','7Kg~%$WRzC',')GMEvtmlLGd','dCZUVRH','kYuq',"EJSMu?v9a","dB4"])
pa_HLB9Dc8L="X b}U"
yCrRhLF=Factor("bmWCjFbSVw[ i]",['GXUYg!<','GRG a0','H?tHHF',"ubwsNtUe1yTh",'zoHJ5ovOzW','hvIEVubmJ7',Level('PslhR;&',2),pa_HLB9Dc8L])

### EXPERIMENT
design=[a4mF8,AryDl2eChY7,yCrRhLF]
crossing=[a4mF8,AryDl2eChY7,yCrRhLF]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3_1"))
### END