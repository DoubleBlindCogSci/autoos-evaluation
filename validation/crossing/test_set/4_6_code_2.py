from sweetpea import *
import os
_dir=os.path.dirname(__file__)
cnsld = Factor("cnsld", ["jgq", "tkdc"])
kkw = Factor("kkw", ["pdko", "ssawmy"])
wumf = Factor("wumf", ["flpf", "xmtpe"])
knyg = Factor("knyg", ["cavibs", "jutybp"])
constraints = []
crossing = [cnsld, kkw, wumf, knyg]


design=[cnsld,kkw,wumf,knyg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_6"))

### END