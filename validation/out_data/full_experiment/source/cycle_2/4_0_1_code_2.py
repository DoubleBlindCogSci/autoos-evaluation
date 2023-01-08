from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
hix = Factor("hix", ["ihhe", "apzae"])
ijkvct = Factor("ijkvct", ["fbww", "fna"])
mowgsv = Factor("mowgsv", ["ihhe", "apzae"])
axw = Factor("axw", ["fbww", "fna"])
constraints = [ExactlyKInARow(3, (ijkvct, "fbww"))]
crossing = [ijkvct, axw]

design=[hix,ijkvct,mowgsv,axw]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0_1"))
