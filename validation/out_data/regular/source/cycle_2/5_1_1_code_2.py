from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jGeqqZm_fQLd = Factor("jGeqqZm}fQLd", [Level("wTs5?jadFEQ", 4), Level("t<AO?", 1), Level("w9hLF?giSBh)", 5), Level("IOl~bYjzwl", 1), Level("jvk3r;CcHD", 1), Level("LzSqYRTdVFkz", 1), Level("G8bJWpRd?", 1)])

design=[jGeqqZm_fQLd]
crossing=[jGeqqZm_fQLd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_1"))

### END
