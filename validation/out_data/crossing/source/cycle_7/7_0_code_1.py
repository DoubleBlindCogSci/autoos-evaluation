from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
quhe = Factor("quhe", ["oqz", "cvgtz"])
qkd = Factor("qkd", ["fkwgkc", "ovb"])
zndnek = Factor("zndnek", ["zaan", "vuvwil"])
ssrm = Factor("ssrm", ["moxd", "vidjt"])
bmnekx = Factor("bmnekx", ["nli", "dkac"])
zymbyg = Factor("zymbyg", ["filecw", "qbbpn"])
lmhje = Factor("lmhje", ["ldipz", "vegiuf"])

### EXPERIMENT
design=[quhe,qkd,zndnek,ssrm,bmnekx,zymbyg,lmhje]
crossing=[[quhe,qkd,zndnek,ssrm,bmnekx,zymbyg,lmhje]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_0"))
### END