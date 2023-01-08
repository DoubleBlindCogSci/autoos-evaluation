from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rngdyp = Factor("rngdyp", ["lgbuee","nvavfs","pxcxcn", "audxtx"])
qjfsc = Factor("qjfsc", ["uematu","bovpo", "duh"])
inq = Factor("inq", ["lfole","doxfz","plm", "qsgdrp"])
txpmmp = Factor("txpmmp", ["eqqykq","eqfo", "hrr"])

### EXPERIMENT
constraints=[ExactlyK(3,(rngdyp,"audxtx")),MinimumTrials(41)]
design=[rngdyp,qjfsc,inq,txpmmp]
crossing=[inq,txpmmp]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1"))
### END