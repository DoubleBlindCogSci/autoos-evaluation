from sweetpea import *
import os
_dir=os.path.dirname(__file__)
kefhtd = Factor("kefhtd", ["guhest", "tjdvjg"])
anrzeu = Factor("anrzeu", ["dfwb", "ppxfb"])
flv = Factor("flv", ["mlrnh", "iioq"])
eoqu = Factor("eoqu", ["rvrtvg", "zxmpu"])
gafnq = Factor("gafnq", ["uyed", "iaorrb"])
tsasmd = Factor("tsasmd", ["uqkrvc", "mgl"])
eabf = Factor("eabf", ["octxf", "gyjk"])
constraints = []
crossing = [[kefhtd, anrzeu, flv], [eoqu, gafnq], [tsasmd, eabf]]


design=[kefhtd,anrzeu,flv,eoqu,gafnq,tsasmd,eabf]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_0"))

### END