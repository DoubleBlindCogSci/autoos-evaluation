from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KDoZlUFmW=Factor("GdBcGBxGo|Rvu>",['EECB','GjQopu[%ZtGx',"[J<tKpw",'fIdGXliLe 0',"g]1nilene]CvZB",'sxI9AEtnCdsoU',"vpZngMRxkoYCe"])

### EXPERIMENT
design=[KDoZlUFmW]
crossing=[KDoZlUFmW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1_0"))
### END