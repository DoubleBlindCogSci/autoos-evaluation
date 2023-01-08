from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rngdyp = Factor("rngdyp", ["lgbuee","nvavfs","pxcxcn", "audxtx"])
qjfsc = Factor("qjfsc", ["uematu","bovpo", "duh"])
inq = Factor("inq", ["lfole","doxfz","plm", "qsgdrp"])
txpmmp = Factor("txpmmp", ["eqqykq","eqfo", "hrr"])


constraints = [MinimumTrials(41), ExactlyK(3,(rngdyp, "audxtx"))]
crossing = [inq, txpmmp]

design=[rngdyp,qjfsc,inq,txpmmp]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END