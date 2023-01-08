from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GseqZ=Level('t<AO?',5)
hdyYOJu='w9hLF?giSBh)'
Sj3GTvL3=Factor("jGeqqZm}fQLd",[Level('wTs5?jadFEQ',4),GseqZ,hdyYOJu,'IOl~bYjzwl','jvk3r;CcHD',"LzSqYRTdVFkz",'G8bJWpRd?'])

### EXPERIMENT
design=[Sj3GTvL3]
crossing=[Sj3GTvL3]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_1"))
### END