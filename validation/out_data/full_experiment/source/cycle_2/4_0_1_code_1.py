from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
hix = Factor("hix", ["ihhe", "apzae"])
ijkvct = Factor("ijkvct", ["fbww", "fna"])
mowgsv = Factor("mowgsv", ["ihhe", "apzae"])
axw = Factor("axw", ["fbww", "fna"])
design=[hix,ijkvct,mowgsv,axw]
constraints=[ExactlyKInARow(3, ijkvct)]
crossing=[ijkvct,axw]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0_1"))
