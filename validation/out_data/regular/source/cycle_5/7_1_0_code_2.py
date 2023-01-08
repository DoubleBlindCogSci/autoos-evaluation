from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

GdBcGBxGo_Rvu_ = Factor("GdBcGBxGo|Rvu>", ["EECB", "GjQopu[%ZtGx", "[J<tKpw", "fIdGXliLe 0", "g]1nilene]CvZB", "sxI9AEtnCdsoU", "vpZngMRxkoYCe"])


design=[GdBcGBxGo_Rvu_]
crossing=[GdBcGBxGo_Rvu_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_1_0"))

### END
