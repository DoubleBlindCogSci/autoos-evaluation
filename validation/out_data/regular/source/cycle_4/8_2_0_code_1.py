from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
g9DfKoc3=['YoYMAfDGWCod','mj*khW(seuB0Mp','IRZO68p~iOeXU',"CSkbjp?E",Level("NXasskD|L",3),'kv{EgJta{Qt',"2oe9",Level("rOjFiahJWANwA",4)]
lb4EG_=Factor('vtYW<WZFqFRj',g9DfKoc3)
agy1uU8V=Factor(")FhOKmtzJr",["Fz|wopq","KoMHGEg",'Ik)U','rL%a','c$i',"IXZo@Sh","m;UFo:R",'qyy1R'])

### EXPERIMENT
design=[lb4EG_,agy1uU8V]
crossing=[lb4EG_,agy1uU8V]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_2_0"))
### END