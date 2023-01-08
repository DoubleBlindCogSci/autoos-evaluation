from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
phpbdt= Factor("phpbdt", ["xmibby","kvd","uwwtg","mdo","zlfa","ctg"])
def is_jkfrap_lsy(phpbdt):
    return phpbdt[-2] == "kvd" and phpbdt[-1] != "kvd"
def is_jkfrap_fxiti(phpbdt):
    return phpbdt[-2] != "kvd" and phpbdt[-1] == "zlfa"
def is_jkfrap_aydm(phpbdt):
    return not (is_jkfrap_lsy(phpbdt) or is_jkfrap_fxiti(phpbdt))
jkfrap= Factor("jkfrap", [DerivedLevel("lsy", Window(is_jkfrap_lsy, [phpbdt], 3, 1)), DerivedLevel("fxiti", Window(is_jkfrap_fxiti, [phpbdt], 3, 1)), DerivedLevel("aydm", Window(is_jkfrap_aydm, [phpbdt], 3, 1))])

design=[phpbdt,jkfrap]
crossing=[jkfrap]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
