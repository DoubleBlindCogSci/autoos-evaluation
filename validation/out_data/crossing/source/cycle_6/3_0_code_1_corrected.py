from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kefhtd = Factor("kefhtd", ["guhest", "tjdvjg"])
anrzeu = Factor("anrzeu", ["dfwb", "ppxfb"])
flv = Factor("flv", ["mlrnh", "iioq"])
eoqu = Factor("eoqu", ["rvrtvg", "zxmpu"])
gafnq = Factor("gafnq", ["uyed", "iaorrb"])
tsasmd = Factor("tsasmd", ["uqkrvc", "mgl"])
eabf = Factor("eabf", ["octxf", "gyjk"])

### EXPERIMENT
design=[kefhtd,anrzeu,flv,eoqu,gafnq,tsasmd,eabf]
crossing = [[kefhtd,anrzeu,flv],[tsasmd,eabf],[eoqu,gafnq],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_0"))
### END
