from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vrq = Factor("vrq", ["dgxe","fngdhc","yreu","wbw","eizq","zhh"])
ouics = Factor("ouics", ["hvjfh","yoibhb","fuaex","aoc","xykbw","wunj"])
def is_chd_iim(vrq, ouics):
    return vrq == "eizq"
def is_chd_lkyk(vrq, ouics):
    return vrq != "eizq" and ouics == "wunj"
def is_chd_eqe(vrq, ouics):
    return not (is_chd_iim(vrq) or is_chd_lkyk(vrq, ouics))
chd = Factor("chd", [DerivedLevel("iim", WithinTrial(is_chd_iim, [vrq])), DerivedLevel("lkyk", WithinTrial(is_chd_lkyk, [vrq, ouics])), DerivedLevel("eqe", WithinTrial(is_chd_eqe, [vrq, ouics]))])

design=[vrq,ouics,chd]
crossing=[chd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END