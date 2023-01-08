from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kbyad = Factor("kbyad", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
jrnzbu = Factor("jrnzbu", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
yepn = Factor("yepn", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
def is_ylp_qwwz(kbyad, jrnzbu, yepn):
    return kbyad[0] == yepn[-1] and kbyad[-1] != jrnzbu[0]
def is_ylp_zqmb(kbyad, jrnzbu, yepn):
    return yepn[-1] != kbyad[0] and kbyad[-1] == jrnzbu[0]
def is_ylp_yqqnsu(kbyad, jrnzbu, yepn):
    return not (is_ylp_qwwz(kbyad, jrnzbu, yepn) or is_ylp_zqmb(kbyad, jrnzbu, yepn))
ylp = Factor("ylp", [DerivedLevel("qwwz", Transition(is_ylp_qwwz, [kbyad, jrnzbu, yepn])), DerivedLevel("zqmb", Transition(is_ylp_zqmb, [kbyad, jrnzbu, yepn])), DerivedLevel("yqqnsu", Transition(is_ylp_yqqnsu, [kbyad, jrnzbu, yepn]))])

design=[kbyad,jrnzbu,yepn,ylp]
crossing=[ylp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END