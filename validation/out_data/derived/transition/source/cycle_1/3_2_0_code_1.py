from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cridpl = Factor("cridpl", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
fra = Factor("fra", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
sqhrna = Factor("sqhrna", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
def yswa(cridpl, fra, sqhrna):
     return fra[-1] == cridpl[0]
def bpic(cridpl, fra, sqhrna):
     return fra[-1] != cridpl[0] and cridpl[-1] == sqhrna[0]
def mio(cridpl, fra, sqhrna):
     return (not yswa(cridpl, fra, sqhrna)) and (not cridpl[-1] == sqhrna[0])
mef = DerivedLevel("vek", Transition(yswa, [cridpl, fra, sqhrna]))
gsfyq = DerivedLevel("nfgszz", Transition(bpic, [cridpl, fra, sqhrna]))
gwuaez = DerivedLevel("fckuoh", Transition(mio, [cridpl, fra, sqhrna]))
dgej = Factor("wjjh", [mef, gsfyq, gwuaez])

### EXPERIMENT
design=[cridpl,fra,sqhrna,dgej]
crossing=[dgej]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END