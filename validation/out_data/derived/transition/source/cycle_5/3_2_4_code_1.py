from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kbyad = Factor("kbyad", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
jrnzbu = Factor("jrnzbu", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
yepn = Factor("yepn", ["eiv","yva","tevh","giswo","xbnkr","pyf","ccky","xdlksn"])
def wwlarp(kbyad, yepn, jrnzbu):
     return kbyad[0] == yepn[-1] and kbyad[-1] != jrnzbu[0]
def qfjsp(kbyad, yepn, jrnzbu):
     return yepn[-1] != kbyad[0] and jrnzbu[0] == kbyad[-1]
def yvfkk(kbyad, yepn, jrnzbu):
     return (not kbyad[0] == yepn[-1]) and (not kbyad[-1] == jrnzbu[0])
rthi = DerivedLevel("qwwz", Transition(wwlarp, [kbyad, jrnzbu, yepn]))
aji = DerivedLevel("zqmb", Transition(qfjsp, [kbyad, jrnzbu, yepn]))
zgr = DerivedLevel("yqqnsu", Transition(yvfkk, [kbyad, jrnzbu, yepn]))
kjrfds = Factor("ylp", [rthi, aji, zgr])

### EXPERIMENT
design=[kbyad,jrnzbu,yepn,kjrfds]
crossing=[kjrfds]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END