from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OGhyxfKA = Factor("OGhyxfKA", [Level("GpIF oIPiLs", 3), "CyJRwFTVSTXbZ", "5>OvauYdNTy", "GIAsZeoe)UW_", "uUkEpboE", "xEhxor_hDDM1xm", "3Ym", "@rcBr", "P{ DbDpbFxUHeX", "qPGg_suDXp)Dy!"])
EEoQq = Factor("EEoQq", ["WGdrC4R", "~HiSlNh", "uZoH", ":POtdtAsg>J", "bJYzMGO", "O390dJsFo", "A4co9Eba(wS:{", "jmG", "lcD", "kCMfMrs", "XwKBLaBs"])

design=[OGhyxfKA,EEoQq]
crossing=[OGhyxfKA,EEoQq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/10_2_1"))

### END
