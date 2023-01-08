from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
szoeft = Factor("szoeft", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
dgtvts = Factor("dgtvts", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
illdc = Factor("illdc", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
def pzj(szoeft, dgtvts, illdc):
     return szoeft[0] == dgtvts[-1] and szoeft[-1] != illdc[0]
def hycg(szoeft, dgtvts, illdc):
     return dgtvts[-1] != szoeft[0] and szoeft[-1] == illdc[0]
def sulrut(szoeft, dgtvts, illdc):
     return (not szoeft[0] == dgtvts[-1]) and (not szoeft[-1] == illdc[0])
illx = Factor("gutkwe", [DerivedLevel("bywbjl", Transition(pzj, [szoeft, dgtvts, illdc])), DerivedLevel("feucje", Transition(hycg, [szoeft, dgtvts, illdc])),DerivedLevel("yawb", Transition(sulrut, [szoeft, dgtvts, illdc]))])
### EXPERIMENT
design=[szoeft,dgtvts,illdc,illx]
crossing=[illx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END