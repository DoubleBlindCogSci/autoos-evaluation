from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vtYW_WZFqFRj = Factor("vtYW<WZFqFRj", [Level("YoYMAfDGWCod", 1), Level("mj*khW(seuB0Mp", 1), Level("IRZO68p~iOeXU", 1), Level("CSkbjp?E", 1), Level("NXasskD|L", 3), Level("kv{EgJta{Qt", 1), Level("2oe9", 1), Level("rOjFiahJWANwA", 4)])
_FhOKmtzJr = Factor(")FhOKmtzJr", [Level("Fz|wopq", 1), Level("KoMHGEg", 1), Level("Ik)U", 1), Level("rL%a", 1), Level("c$i", 1), Level("IXZo@Sh", 1), Level("m;UFo:R", 1), Level("qyy1R", 1)])

design=[vtYW_WZFqFRj,_FhOKmtzJr]
crossing=[vtYW_WZFqFRj,_FhOKmtzJr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_2_0"))

### END
