from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ohixrc = Factor("ohixrc", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
dyt = Factor("dyt", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
pef = Factor("pef", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
def bzbppw(ohixrc, pef, dyt):
     return pef == ohixrc
def liaab(ohixrc, pef, dyt):
     return pef != ohixrc and ohixrc == dyt
def phj(ohixrc, pef, dyt):
     return (not ohixrc == pef) and (ohixrc != dyt)
qilxs = Factor("zfoyvj", [DerivedLevel("lqk", WithinTrial(bzbppw, [ohixrc, dyt, pef])), DerivedLevel("skpe", WithinTrial(liaab, [ohixrc, dyt, pef])),DerivedLevel("yudp", WithinTrial(phj, [ohixrc, dyt, pef]))])
### EXPERIMENT
design=[ohixrc,dyt,pef,qilxs]
crossing=[qilxs]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END