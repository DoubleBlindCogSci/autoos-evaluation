from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nojea_nz__Eb = Factor("nojea7nz7?Eb", [Level("%Z}", 1), Level("yaw", 3), Level("OOab$%JUR", 1), Level("LYT", 1), Level("hheFg", 1), Level("YRwAXw", 1), Level("~xxjZEUaIbqR6", 4), Level("VAAiZx", 1)])
__gupuVfSeK = Factor("!>gupuVfSeK", ["PfTiRZJWRrX^u", "qKMAU", "qLX~v", "Q(L(FafcBoR ", "FCSk;oW", "blu", "OR SOfdt0aKE", "VJ&HI~LLdmaRD"])
qBnJwyqc = Factor("qBnJwyqc", [Level("3Q|9", 2), Level("?gTNAXGea&", 1), Level("qYYY", 2), Level("aoJ3", 1), Level("qlZO$txitrcnc", 1), Level("FDJf", 1), Level("f;iW@bs", 1), Level("s9LfnOlKQpFt", 1)])

design=[nojea_nz__Eb,__gupuVfSeK,qBnJwyqc]
crossing=[nojea_nz__Eb,__gupuVfSeK,qBnJwyqc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_3_0"))

### END
