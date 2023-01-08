from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qpc = Factor("qpc", ["sxjfsk","ytsqt","zgbjsi", "utq"])
xcwoli = Factor("xcwoli", ["syn","yrqvbi","sjbbe", "tax"])
tkdy = Factor("tkdy", ["djt","pct","kuz", "hcl"])
yqwy = Factor("yqwy", ["cuwak","bzhmtp","dhz", "ucg"])

### EXPERIMENT
constraints=[ExactlyKInARow(3,(qpc,"utq")),ExactlyK(2,(xcwoli,"tax"))]
design=[qpc,xcwoli,tkdy,yqwy]
crossing=[tkdy,yqwy]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_4"))
### END