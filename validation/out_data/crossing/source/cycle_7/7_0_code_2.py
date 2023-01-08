from sweetpea import *
import os
_dir=os.path.dirname(__file__)
quhe = Factor("quhe", ["oqz", "cvgtz"])
qkd = Factor("qkd", ["fkwgkc", "ovb"])
zndnek = Factor("zndnek", ["zaan", "vuvwil"])
ssrm = Factor("ssrm", ["moxd", "vidjt"])
bmnekx = Factor("bmnekx", ["nli", "dkac"])
zymbyg = Factor("zymbyg", ["filecw", "qbbpn"])
lmhje = Factor("lmhje", ["ldipz", "vegiuf"])
constraints = []
crossing = [quhe, qkd, zndnek, ssrm, bmnekx, zymbyg, lmhje]


design=[quhe,qkd,zndnek,ssrm,bmnekx,zymbyg,lmhje]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_0"))

### END