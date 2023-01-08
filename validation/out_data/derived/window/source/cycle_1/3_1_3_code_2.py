from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tqywwe= Factor("tqywwe", ["jep","givaf","dshe","hvdbkc","antde","mqan","ceb"])
def is_xcic_lfli(tqywwe):
    return tqywwe[0] == "dshe"
def is_xcic_fovsd(tqywwe):
    return tqywwe[0] == "givaf"
def is_xcic_sfo(tqywwe):
    return not (is_xcic_lfli(tqywwe) or is_xcic_fovsd(tqywwe))
xcic= Factor("xcic", [DerivedLevel("lfli", Window(is_xcic_lfli, [tqywwe], 3, 1)), DerivedLevel("fovsd", Window(is_xcic_fovsd, [tqywwe], 3, 1)), DerivedLevel("sfo", Window(is_xcic_sfo, [tqywwe], 3, 1))])

design=[tqywwe,xcic]
crossing=[xcic]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
