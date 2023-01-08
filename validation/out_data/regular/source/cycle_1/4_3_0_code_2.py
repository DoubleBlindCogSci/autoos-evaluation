from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DGMf= Factor("DGMf", ["KFBYQRG$t(8Rt", ":evlU^Da0n", "fkMsUUrrVwnq", "EYtgegWyFLEZC"])
_BqTAtQZR= Factor("$BqTAtQZR", [Level("deuc_<b", 3), "Qnm[)WPhY", "CPvx", ";Eskx"])
RJdhjTrR_= Factor("RJdhjTrR)", ["vAONvJuQMfDD", "KX%LpLfwX", "tL10fRF|iM", "@Ey"])

design=[DGMf,_BqTAtQZR,RJdhjTrR_]
crossing=[DGMf,_BqTAtQZR,RJdhjTrR_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_3_0"))

### END
