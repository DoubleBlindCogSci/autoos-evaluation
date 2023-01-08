from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dwrpg= Factor("dwrpg", ["kjdt","syccui","nuzuca","jbwexv","fayn","vut"])
ossys= Factor("ossys", ["jvvyw","xru","juns","bct","slm","gunfs","rijlq","mykt"])
def is_itia_zphjm(dwrpg):
    return dwrpg[0] == "kjdt"
def is_itia_cgtyi(dwrpg, ossys):
    return dwrpg[0] != "kjdt" and ossys[0] == "juns"
def is_itia_ugeqmm(dwrpg, ossys):
    return not (is_itia_zphjm(dwrpg) or is_itia_cgtyi(dwrpg, ossys))
itia= Factor("itia", [DerivedLevel("zphjm", Transition(is_itia_zphjm, [dwrpg])), DerivedLevel("cgtyi", Transition(is_itia_cgtyi, [dwrpg, ossys])), DerivedLevel("ugeqmm", Transition(is_itia_ugeqmm, [dwrpg, ossys]))])

design=[dwrpg,ossys,itia]
crossing=[itia]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
