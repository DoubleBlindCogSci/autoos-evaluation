from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hwdb = Factor("hwdb", ["uhhgjg","wkwuq","qtj","igw","eoxdtw","dbss","sgw","grdt"])
gderh = Factor("gderh", ["uga","ziq","tswnb","mxgf","aqgxnv","hlx"])
def eduf(hwdb, gderh):
     return "eoxdtw" == hwdb[-1] and gderh[0] != "mxgf"
def qgv(hwdb, gderh):
     return hwdb[-1] != "eoxdtw" and gderh[0] == "mxgf"
def ezhwo(hwdb, gderh):
     return (not hwdb[-1] == "eoxdtw") and (not qgv(hwdb, gderh))
psef = Factor("xtw", [DerivedLevel("rjw", Transition(eduf, [hwdb, gderh])), DerivedLevel("wze", Transition(qgv, [hwdb, gderh])),DerivedLevel("iygzzo", Transition(ezhwo, [hwdb, gderh]))])
### EXPERIMENT
design=[hwdb,gderh,psef]
crossing=[psef]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END