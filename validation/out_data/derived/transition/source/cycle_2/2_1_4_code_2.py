from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
puuirx= Factor("puuirx", ["nheqg","jjntjd","elcml","emhaui","vhijf"])
def is_sranze_tmy(puuirx):
    return puuirx[0] != "jjntjd" and puuirx[-1] != "vhijf"
def is_sranze_kklmdf(puuirx):
    return not is_sranze_tmy(puuirx)
sranze= Factor("sranze", [DerivedLevel("tmy", Transition(is_sranze_tmy, [puuirx])), DerivedLevel("kklmdf", Transition(is_sranze_kklmdf, [puuirx]))])

design=[puuirx,sranze]
crossing=[sranze]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
