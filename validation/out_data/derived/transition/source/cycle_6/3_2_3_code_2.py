from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hwdb = Factor("hwdb", ["uhhgjg","wkwuq","qtj","igw","eoxdtw","dbss","sgw","grdt"])
gderh = Factor("gderh", ["uga","ziq","tswnb","mxgf","aqgxnv","hlx"])
def is_xtw_rjw(hwdb, gderh):
    return hwdb[-1] == "eoxdtw" and gderh[0] != "mxgf"
def is_xtw_wze(hwdb, gderh):
    return hwdb[-1] != "eoxdtw" and gderh[0] == "mxgf"
def is_xtw_iygzzo(hwdb, gderh):
    return not (is_xtw_rjw(hwdb, gderh) or is_xtw_wze(hwdb, gderh))
xtw = Factor("xtw", [DerivedLevel("rjw", Transition(is_xtw_rjw, [hwdb, gderh])), DerivedLevel("wze", Transition(is_xtw_wze, [hwdb, gderh])), DerivedLevel("iygzzo", Transition(is_xtw_iygzzo, [hwdb, gderh]))])

design=[hwdb,gderh,xtw]
crossing=[xtw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END