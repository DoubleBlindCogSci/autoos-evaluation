from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xoy = Factor("xoy", ["pxh", "yyoerd"])
enxal = Factor("enxal", ["fooego", "nvkk"])
lcxe = Factor("lcxe", ["ymxua", "ttx"])
klsb = Factor("klsb", ["lbjxpl", "futrp"])
fllfip = Factor("fllfip", ["vsl", "eqf"])
axig = Factor("axig", ["dpn", "qqaf"])
brzoqj = Factor("brzoqj", ["asdbj", "nqz"])

### EXPERIMENT
design=[xoy,enxal,lcxe,klsb,fllfip,axig,brzoqj]
crossing=[[xoy],[enxal,lcxe,klsb],[fllfip],[axig,brzoqj],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1"))
### END