from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qgpi = Factor("qgpi", ["xgstwk","wknoj","jgcumv","ujvch","fkw"])
def is_enos_sdrcc(qgpi):
    return qgpi[0] != "jgcumv" or qgpi[-2] == "wknoj"
def is_enos_osk(qgpi):
    return not is_enos_sdrcc(qgpi)
enos = Factor("enos", [DerivedLevel("sdrcc", Window(is_enos_sdrcc, [qgpi], 3, 1)), DerivedLevel("osk", Window(is_enos_osk, [qgpi], 3, 1))])

design=[qgpi,enos]
crossing=[enos]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END