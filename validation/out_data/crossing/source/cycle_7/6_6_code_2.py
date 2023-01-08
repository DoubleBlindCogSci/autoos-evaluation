from sweetpea import *
import os
_dir=os.path.dirname(__file__)
bzayws = Factor("bzayws", ["qyhh", "mdwens"])
xhrfl = Factor("xhrfl", ["acg", "busj"])
aquf = Factor("aquf", ["zvf", "egco"])
xcw = Factor("xcw", ["wnplqq", "hgth"])
yta = Factor("yta", ["epf", "jwph"])
qqeazh = Factor("qqeazh", ["enba", "baer"])
constraints = []
crossing = [bzayws, xhrfl, aquf, xcw, yta, qqeazh]


design=[bzayws,xhrfl,aquf,xcw,yta,qqeazh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_6"))

### END