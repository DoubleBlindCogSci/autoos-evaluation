from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wjnax = Factor("wjnax", ["wlxyd","zrql","xmrrwb","hsq","vncl","etbr"])
def is_samck_noxy(wjnax):
    return wjnax[0] == "xmrrwb" and wjnax[-3] != "xmrrwb"
def is_samck_joc(wjnax):
    return wjnax[0] != "xmrrwb" and wjnax[-3] == "vncl"
def is_samck_bwit(wjnax):
    return not (is_samck_noxy(wjnax) or is_samck_joc(wjnax))
samck= Factor("samck", [DerivedLevel("noxy", Window(is_samck_noxy, [wjnax], 4, 1)), DerivedLevel("joc", Window(is_samck_joc, [wjnax], 4, 1)), DerivedLevel("bwit", Window(is_samck_bwit, [wjnax], 4, 1))])

design=[wjnax,samck]
crossing=[samck]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
