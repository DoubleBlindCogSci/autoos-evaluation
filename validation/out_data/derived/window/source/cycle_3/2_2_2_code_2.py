from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yemhmd = Factor("yemhmd", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
fhpxgk = Factor("fhpxgk", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
hbf = Factor("hbf", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
def is_xai_ejfrf(yemhmd, fhpxgk, hbf):
    return yemhmd[-3] != hbf[-2]
def is_xai_ytxwau(yemhmd, fhpxgk, hbf):
    return not is_xai_ejfrf(yemhmd, fhpxgk, hbf)
xai= Factor("xai", [DerivedLevel("ejfrf", Window(is_xai_ejfrf, [yemhmd, fhpxgk, hbf], 4, 1)), DerivedLevel("ytxwau", Window(is_xai_ytxwau, [yemhmd, fhpxgk, hbf], 4, 1))])

design=[yemhmd,fhpxgk,hbf,xai]
crossing=[xai]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
