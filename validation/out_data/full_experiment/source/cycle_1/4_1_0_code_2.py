from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
vsjz = Factor("vsjz", ["sjui", "ikecv"])
jko = Factor("jko", ["bqht", "weiurp"])
smcarz = Factor("smcarz", ["sjui", "ikecv"])
khud = Factor("khud", ["bqht", "weiurp"])
def is_zwizsh_inny(khud, vsjz):
    return khud == vsjz
def is_zwizsh_foini(khud, vsjz):
    return not is_zwizsh_inny(khud, vsjz)
zwizsh = Factor("zwizsh", [DerivedLevel("inny", WithinTrial(is_zwizsh_inny, [khud, vsjz])), DerivedLevel("foini", WithinTrial(is_zwizsh_foini, [khud, vsjz]))])
constraints = []
crossing = [smcarz, khud]

design=[vsjz,jko,smcarz,khud,zwizsh]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_1_0"))
