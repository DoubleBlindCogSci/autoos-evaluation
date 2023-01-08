from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wjnax = Factor("wjnax", ["wlxyd","zrql","xmrrwb","hsq","vncl","etbr"])
def bwfz(wjnax):
     return wjnax[0] == "xmrrwb" and not wjnax[-3] == "xmrrwb"
def wsfrj(wjnax):
     return wjnax[0] != "xmrrwb" and  wjnax[-3] == "vncl"
def ybn(wjnax):
     return (wjnax[0] != "xmrrwb") and (not wsfrj(wjnax))
jinl = DerivedLevel("noxy", Window(bwfz, [wjnax],4,1))
vvchk = DerivedLevel("joc", Window(wsfrj, [wjnax],4,1))
vvrhv = DerivedLevel("bwit", Window(ybn, [wjnax],4,1))
ewdyz = Factor("samck", [jinl, vvchk, vvrhv])

### EXPERIMENT
design=[wjnax,ewdyz]
crossing=[ewdyz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END