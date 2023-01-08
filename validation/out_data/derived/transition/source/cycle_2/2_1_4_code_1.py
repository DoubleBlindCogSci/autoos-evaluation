from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
puuirx = Factor("puuirx", ["nheqg","jjntjd","elcml","emhaui","vhijf"])
def vrvgw(puuirx):
    return puuirx[0] != "jjntjd" and puuirx[-1] != "vhijf"
def yfhkcq(puuirx):
    return not (puuirx[0] != "jjntjd") or not (puuirx[0] != "vhijf")
ffshdj = DerivedLevel("tmy", Transition(vrvgw, [puuirx]))
xyrk = DerivedLevel("kklmdf", Transition(yfhkcq, [puuirx]))
qwgbil = Factor("sranze", [ffshdj, xyrk])

### EXPERIMENT
design=[puuirx,qwgbil]
crossing=[qwgbil]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END