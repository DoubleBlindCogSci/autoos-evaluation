from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ppo = Factor("ppo", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
vjsf = Factor("vjsf", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
utvdc = Factor("utvdc", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
def lkianh(ppo, utvdc, vjsf):
    return ppo[0] != utvdc[-1] and ppo[-1] == vjsf[0]
def groddj(ppo, utvdc, vjsf):
    return not lkianh(ppo, utvdc, vjsf)
oli = DerivedLevel("szx", Transition(lkianh, [ppo, vjsf, utvdc]))
swzbr = DerivedLevel("dvcood", Transition(groddj, [ppo, vjsf, utvdc]))
elvuso = Factor("paqaim", [oli, swzbr])

### EXPERIMENT
design=[ppo,vjsf,utvdc,elvuso]
crossing=[elvuso]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END