from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vzweak= Factor("vzweak", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
dsrncz= Factor("dsrncz", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
nwdg= Factor("nwdg", ["dac","akj","zrqmsu","sauji","mkcqu","iqky"])
def is_cij_gkutnp(vzweak, dsrncz, nwdg):
    return dsrncz[-1] == vzweak[0] and vzweak[-1] != nwdg[0]
def is_cij_qpmdhc(vzweak, dsrncz, nwdg):
    return dsrncz[-1] != vzweak[0] and vzweak[-1] == nwdg[0]
def is_cij_ezj(vzweak, dsrncz, nwdg):
    return not (is_cij_gkutnp(vzweak, dsrncz, nwdg) or is_cij_qpmdhc(vzweak, dsrncz, nwdg))
cij= Factor("cij", [DerivedLevel("gkutnp", Transition(is_cij_gkutnp, [vzweak, dsrncz, nwdg])), DerivedLevel("qpmdhc", Transition(is_cij_qpmdhc, [vzweak, dsrncz, nwdg])), DerivedLevel("ezj", Transition(is_cij_ezj, [vzweak, dsrncz, nwdg]))])

design=[vzweak,dsrncz,nwdg,cij]
crossing=[cij]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
