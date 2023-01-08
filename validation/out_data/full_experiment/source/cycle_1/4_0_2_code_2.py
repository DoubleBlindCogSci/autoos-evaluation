from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
vrern = Factor("vrern", ["ofdjhs", "ansm"])
nfi = Factor("nfi", ["ofxmh", "lyvsf"])
esewp = Factor("esewp", ["ofdjhs", "ansm"])
ffr = Factor("ffr", ["ofxmh", "lyvsf"])
constraints = [AtMostKInARow(3, esewp), AtLeastKInARow(4, ffr)]
crossing = [ffr, esewp]

design=[vrern,nfi,esewp,ffr]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_0_2"))
