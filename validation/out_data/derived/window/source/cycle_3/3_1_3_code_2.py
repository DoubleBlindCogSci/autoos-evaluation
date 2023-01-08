from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
myriv = Factor("myriv", ["rix","czbk","ryyilj","lmmecb","rungn","iex"])
def is_jpu_tkiu(myriv):
    return myriv[-2] == "rix" and myriv[0] != "rix"
def is_jpu_nxmsiz(myriv):
    return myriv[-2] != "rix" and myriv[0] == "czbk"
def is_jpu_nandlu(myriv):
    return not (is_jpu_tkiu(myriv) or is_jpu_nxmsiz(myriv))
jpu= Factor("jpu", [DerivedLevel("tkiu", Window(is_jpu_tkiu, [myriv], 3, 1)), DerivedLevel("nxmsiz", Window(is_jpu_nxmsiz, [myriv], 3, 1)), DerivedLevel("nandlu", Window(is_jpu_nandlu, [myriv], 3, 1))])

design=[myriv,jpu]
crossing=[jpu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
