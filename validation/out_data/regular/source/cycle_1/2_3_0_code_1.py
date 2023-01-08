from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
A7QDPGygnJz=Factor('HtCPuxXG',[Level('mUWJ[VHkU',1),'pDaTAkwbK['])
fgwj05dIyzg=Factor("x&}VYLN",["INxF(e5pv","lNzHD"])
cATUTyRV8R=Factor('gHs',["BkFi3BXfDs6dZ","HVdvc&>;<iZ*"])

### EXPERIMENT
design=[A7QDPGygnJz,fgwj05dIyzg,cATUTyRV8R]
crossing=[A7QDPGygnJz,fgwj05dIyzg,cATUTyRV8R]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/2_3_0"))
### END