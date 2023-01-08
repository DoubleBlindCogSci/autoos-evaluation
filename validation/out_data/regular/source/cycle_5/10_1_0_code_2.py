from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
igTjkO = Factor("igTjkO", [Level("lXSSSdp", 1), Level("UUUSnRt", 2), "cQBpBE[s", ")Bgv?4U@", "mWvKs", "0Gw", "?~funMrkJeN8", "h4myF6nA", ";g;wRRu", "UmKsYV8%"])

design=[igTjkO]
crossing=[igTjkO]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/10_1_0"))

### END
