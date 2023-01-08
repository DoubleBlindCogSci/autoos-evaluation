from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
szoeft= Factor("szoeft", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
dgtvts= Factor("dgtvts", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
illdc= Factor("illdc", ["dqossz","arkqr","ted","zaghzc","jnlat","xqbh","nsetdb","ijbl"])
def is_gutkwe_bywbjl(szoeft, dgtvts, illdc):
    return szoeft[0] == dgtvts[-1] and szoeft[-1] != illdc[0]
def is_gutkwe_feucje(szoeft, dgtvts, illdc):
    return dgtvts[-1] != szoeft[0] and szoeft[-1] == illdc[0]
def is_gutkwe_yawb(szoeft, dgtvts, illdc):
    return not (is_gutkwe_bywbjl(szoeft, dgtvts, illdc) or is_gutkwe_feucje(szoeft, dgtvts, illdc))
gutkwe= Factor("gutkwe", [DerivedLevel("bywbjl", Transition(is_gutkwe_bywbjl, [szoeft, dgtvts, illdc])), DerivedLevel("feucje", Transition(is_gutkwe_feucje, [szoeft, dgtvts, illdc])), DerivedLevel("yawb", Transition(is_gutkwe_yawb, [szoeft, dgtvts, illdc]))])

design=[szoeft,dgtvts,illdc,gutkwe]
crossing=[gutkwe]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END
