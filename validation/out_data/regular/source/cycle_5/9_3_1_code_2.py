from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ScY = Factor("ScY", [Level("kvzBaS9p", 2), "2xNBOUjVPlN", "pkZPC<hdr", "?BpoR", "LBiAoA$fZbCv", "nDKyhot", "s_ofo", "haD0euQ", "uNwxfRC"])
EOOJTns_VdPxM = Factor("EOOJTns5VdPxM", ["oJf#N", "GY2AXx[*", "^uQ}gRj", "YmTZuAu", "0voYsEWkjXCB", "bXB%GKCW", "QiyzS6", "p4izJliG", "B65", "iehc"])
d_u = Factor("d9u", [Level("srHT", 1), "GHyUECmTKDKN", "rN pex", "4BEbAVO", "Bn@wDLlZA", "GDO", "qc2KMQkxL7", Level("0qnEZKMkJ", 4), "rifENTgudZ", "r2KTgU"])

design=[ScY,EOOJTns_VdPxM,d_u]
crossing=[ScY,EOOJTns_VdPxM,d_u]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_3_1"))

### END
