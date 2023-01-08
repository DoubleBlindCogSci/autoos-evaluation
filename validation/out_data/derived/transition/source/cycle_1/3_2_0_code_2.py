from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cridpl= Factor("cridpl", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
fra= Factor("fra", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
sqhrna= Factor("sqhrna", ["hdv","imqaa","klbnd","kicbz","bfasj","cievtk","iqser"])
def is_wjjh_vek(fra, cridpl):
    return fra[0] == cridpl[-1]
def is_wjjh_nfgszz(fra, cridpl, sqhrna):
    return fra[0] != cridpl[-1] and cridpl[0] == sqhrna[-1]
def is_wjjh_fckuoh(fra, cridpl, sqhrna):
    return not (is_wjjh_vek(fra, cridpl) or is_wjjh_nfgszz(fra, cridpl, sqhrna))
wjjh= Factor("wjjh", [DerivedLevel("vek", Transition(is_wjjh_vek, [fra, cridpl])), DerivedLevel("nfgszz", Transition(is_wjjh_nfgszz, [fra, cridpl, sqhrna])), DerivedLevel("fckuoh", Transition(is_wjjh_fckuoh, [fra, cridpl, sqhrna]))])

design=[cridpl,fra,sqhrna,wjjh]
crossing=[wjjh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
