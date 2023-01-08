from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pcqwk = Factor("pcqwk", ["kpqzyd","illtb","eqvg","brs","vrjjde","awal","sqdls"])
def is_jnvu_cysage(pcqwk):
    return pcqwk[0] == "sqdls" and pcqwk[-1] != "sqdls"
def is_jnvu_ayui(pcqwk):
    return pcqwk[0] != "sqdls" and pcqwk[-1] == "illtb"
def is_jnvu_tevdko(pcqwk):
    return not (is_jnvu_cysage(pcqwk) or is_jnvu_ayui(pcqwk))
jnvu = Factor("jnvu", [DerivedLevel("cysage", Window(is_jnvu_cysage, [pcqwk], 2, 1)), DerivedLevel("ayui", Window(is_jnvu_ayui, [pcqwk], 2, 1)), DerivedLevel("tevdko", Window(is_jnvu_tevdko, [pcqwk], 2, 1))])

design=[pcqwk,jnvu]
crossing=[jnvu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END