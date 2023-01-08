from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uqwxh = Factor("uqwxh", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
vwoe = Factor("vwoe", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
ckstue = Factor("ckstue", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
def is_kjq_mfqks(uqwxh, vwoe, ckstue):
    return uqwxh[-3] == ckstue[0] and uqwxh[0] != vwoe[-3]
def is_kjq_ifgsok(uqwxh, vwoe, ckstue):
    return ckstue[0] != uqwxh[-3] and uqwxh[0] == vwoe[-3]
def is_kjq_xywkiw(uqwxh, vwoe, ckstue):
    return not (is_kjq_mfqks(uqwxh, vwoe, ckstue) or is_kjq_ifgsok(uqwxh, vwoe, ckstue))
kjq= Factor("kjq", [DerivedLevel("mfqks", Window(is_kjq_mfqks, [uqwxh, vwoe, ckstue], 4, 1)), DerivedLevel("ifgsok", Window(is_kjq_ifgsok, [uqwxh, vwoe, ckstue], 4, 1)), DerivedLevel("xywkiw", Window(is_kjq_xywkiw, [uqwxh, vwoe, ckstue], 4, 1))])

design=[uqwxh,vwoe,ckstue,kjq]
crossing=[kjq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END