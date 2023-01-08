from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kxpgtn = Factor("kxpgtn", ["ptii","yqq", "jfbj"])
twqlft = Factor("twqlft", ["thcf","vdz", "lic"])
ixez = Factor("ixez", ["nvxmit","kst","wrbe", "xvv"])
qmocmz = Factor("qmocmz", ["vhlgxv", "uupiw"])


constraints = [Exclude((kxpgtn, "jfbj")), ExactlyKInARow(3, (twqlft, "lic")), AtMostKInARow(2, (ixez, "xvv"))]
crossing = [qmocmz]

design=[kxpgtn,twqlft,ixez,qmocmz]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3"))

### END