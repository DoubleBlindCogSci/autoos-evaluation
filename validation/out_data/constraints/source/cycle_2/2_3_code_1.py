from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
amksb = Factor("amksb", ["skg","wyxuu", "ijewh"])
wxr = Factor("wxr", ["mctktb", "qtbq"])
fmyu = Factor("fmyu", ["uqes","efye", "wwb"])
oskzuv = Factor("oskzuv", ["cslpba", "jwcaot"])

### EXPERIMENT
constraints=[ExactlyKInARow(3,(amksb,"ijewh")),AtLeastKInARow(2,(wxr,"qtbq"))]
design=[amksb,wxr,fmyu,oskzuv]
crossing=[fmyu,oskzuv]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3"))
### END