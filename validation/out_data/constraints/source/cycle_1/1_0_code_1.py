from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rhlqtt = Factor("rhlqtt", ["spaqpf","eols", "gmjo"])
osd = Factor("osd", ["ljh","tmg", "cyiv"])
jaxz = Factor("jaxz", ["hou","try","qmtxtw", "xbkj"])
sjln = Factor("sjln", ["hmdy", "pndj"])

### EXPERIMENT
constraints=[ExactlyK(4,(rhlqtt,"gmjo"))]
design=[rhlqtt,osd,jaxz,sjln]
crossing=[osd,jaxz,sjln]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_0"))
### END