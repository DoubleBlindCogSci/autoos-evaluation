from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yemhmd = Factor("yemhmd", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
fhpxgk = Factor("fhpxgk", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
hbf = Factor("hbf", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
def gnidds(yemhmd, hbf, fhpxgk):
    return yemhmd[-3] != hbf[-2]
def ram(yemhmd, hbf, fhpxgk):
    return not (yemhmd[-3] != hbf[-2])
fjnik = DerivedLevel("ejfrf", Window(gnidds, [yemhmd, fhpxgk, hbf],4,1))
cfxgf = DerivedLevel("ytxwau", Window(ram, [yemhmd, fhpxgk, hbf],4,1))
jlhqr = Factor("xai", [fjnik, cfxgf])

### EXPERIMENT
design=[yemhmd,fhpxgk,hbf,jlhqr]
crossing=[jlhqr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END