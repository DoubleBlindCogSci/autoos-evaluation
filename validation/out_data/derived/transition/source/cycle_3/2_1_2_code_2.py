from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oeiu = Factor("oeiu", ["mjbpsw","mbe","ujudp","hwx","xgi","exofud"])
def is_qfre_sopit(oeiu):
    return oeiu[-1] != "ujudp" and oeiu[0] == "mbe"
def is_qfre_alor(oeiu):
    return not is_qfre_sopit(oeiu)
qfre= Factor("qfre", [DerivedLevel("sopit", Transition(is_qfre_sopit, [oeiu])), DerivedLevel("alor", Transition(is_qfre_alor, [oeiu]))])

design=[oeiu,qfre]
crossing=[qfre]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
