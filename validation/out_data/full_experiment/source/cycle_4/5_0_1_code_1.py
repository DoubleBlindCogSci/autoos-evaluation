from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
opth = Factor("opth", ["cupxsi", "jehney"])
jtwon = Factor("jtwon", ["nupd", "tkkn"])
qgaatu = Factor("qgaatu", ["cupxsi", "jehney"])
cnekt = Factor("cnekt", ["nupd", "tkkn"])
ryuvgo = Factor("ryuvgo", ["hsm", "ghlii"])
design=[opth,jtwon,qgaatu,cnekt,ryuvgo]
constraints=[ExactlyKInARow(4, cnekt)]
crossing=[cnekt,jtwon]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_1"))
