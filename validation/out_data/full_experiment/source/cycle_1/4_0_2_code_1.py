from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
vrern = Factor("vrern", ["ofdjhs", "ansm"])
nfi = Factor("nfi", ["ofxmh", "lyvsf"])
esewp = Factor("esewp", ["ofdjhs", "ansm"])
ffr = Factor("ffr", ["ofxmh", "lyvsf"])
design=[vrern,nfi,esewp,ffr]
constraints=[AtMostKInARow(3, esewp),AtLeastKInARow(4, ffr)]
crossing=[ffr,esewp]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_0_2"))
