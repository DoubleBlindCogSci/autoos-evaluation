from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rfywt = Factor("rfywt", ["oyynyz","xpsg","pmyxq","pqqcj","udo","zfbwh"])
ofxt = Factor("ofxt", ["tktvw","rxqy","cdyvqp","jcfa","tiwln","qcspc"])
def is_cczo_ayn(rfywt, ofxt):
    return rfywt[0] == "udo" or ofxt[-1] != "rxqy"
def is_cczo_dfomek(rfywt, ofxt):
    return not is_cczo_ayn(rfywt, ofxt)
cczo = Factor("cczo", [DerivedLevel("ayn", Window(is_cczo_ayn, [rfywt, ofxt], 2, 1)), DerivedLevel("dfomek", Window(is_cczo_dfomek, [rfywt, ofxt], 2, 1))])

design=[rfywt,ofxt,cczo]
crossing=[cczo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END