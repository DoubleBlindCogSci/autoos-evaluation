from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jzn = Factor("jzn", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
ehon = Factor("ehon", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
xtzkge = Factor("xtzkge", ["jghcja","dbd","gxellq","ivxlp","qjdrcn","qglutk","zof"])
def is_kultts_wrn(jzn, ehon, xtzkge):
    return jzn[-2] == xtzkge[0] and jzn[0] != ehon[-2]
def is_kultts_yrit(jzn, ehon, xtzkge):
    return not is_kultts_wrn(jzn, ehon, xtzkge)
kultts= Factor("kultts", [DerivedLevel("wrn", Window(is_kultts_wrn, [jzn, ehon, xtzkge], 3, 1)), DerivedLevel("yrit", Window(is_kultts_yrit, [jzn, ehon, xtzkge], 3, 1))])

design=[jzn,ehon,xtzkge,kultts]
crossing=[kultts]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
