from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rfywt = Factor("rfywt", ["oyynyz","xpsg","pmyxq","pqqcj","udo","zfbwh"])
ofxt = Factor("ofxt", ["tktvw","rxqy","cdyvqp","jcfa","tiwln","qcspc"])
def xjvv(rfywt, ofxt):
    return rfywt[0] == "udo" or ofxt[-1] != "rxqy"
def iqykd(rfywt,ofxt):
    return not xjvv(rfywt, ofxt)
dbe = Factor("cczo", [DerivedLevel("ayn", Window(xjvv, [rfywt, ofxt],2,1)), DerivedLevel("dfomek", Window(iqykd, [rfywt, ofxt],2,1))])
### EXPERIMENT
design=[rfywt,ofxt,dbe]
crossing=[dbe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END