from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
opth = Factor("opth", ["cupxsi", "jehney"])
jtwon = Factor("jtwon", ["nupd", "tkkn"])
qgaatu = Factor("qgaatu", ["cupxsi", "jehney"])
cnekt = Factor("cnekt", ["nupd", "tkkn"])
ryuvgo = Factor("ryuvgo", ["hsm", "ghlii"])
constraints = [ExactlyKInARow(4, (cnekt, "nupd"))]
crossing = [cnekt, jtwon]

design=[opth,jtwon,qgaatu,cnekt,ryuvgo]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_0_1"))
