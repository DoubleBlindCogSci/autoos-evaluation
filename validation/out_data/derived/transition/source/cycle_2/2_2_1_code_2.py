from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ppo= Factor("ppo", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
vjsf= Factor("vjsf", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
utvdc= Factor("utvdc", ["upntt","cozzx","vja","usdt","piruj","qslry","qlb"])
def is_paqaim_szx(ppo, vjsf, utvdc):
    return ppo[0] != utvdc[-1] and ppo[-1] == vjsf[0]
def is_paqaim_dvcood(ppo, vjsf, utvdc):
    return not is_paqaim_szx(ppo, vjsf, utvdc)
paqaim= Factor("paqaim", [DerivedLevel("szx", Transition(is_paqaim_szx, [ppo, vjsf, utvdc])), DerivedLevel("dvcood", Transition(is_paqaim_dvcood, [ppo, vjsf, utvdc]))])

design=[ppo,vjsf,utvdc,paqaim]
crossing=[paqaim]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
