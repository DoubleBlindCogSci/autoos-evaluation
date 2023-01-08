from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pqdejc = Factor("pqdejc", ["yhvz","vumfbe","tavubn","okanp","hoaem","edsktp"])
def is_piqz_ksm(pqdejc):
    return pqdejc[0] == "okanp" and pqdejc[-1] != "okanp"
def is_piqz_njg(pqdejc):
    return pqdejc[0] != "okanp" and pqdejc[-2] == "edsktp"
def is_piqz_dbkie(pqdejc):
    return not (is_piqz_ksm(pqdejc) or is_piqz_njg(pqdejc))
piqz= Factor("piqz", [DerivedLevel("ksm", Window(is_piqz_ksm, [pqdejc], 3, 1)), DerivedLevel("njg", Window(is_piqz_njg, [pqdejc], 3, 1)), DerivedLevel("dbkie", Window(is_piqz_dbkie, [pqdejc], 3, 1))])

design=[pqdejc,piqz]
crossing=[piqz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END