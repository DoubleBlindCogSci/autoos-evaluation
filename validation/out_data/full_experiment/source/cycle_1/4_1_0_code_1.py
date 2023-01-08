from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
vsjz = Factor("vsjz", ["sjui", "ikecv"])
jko = Factor("jko", ["bqht", "weiurp"])
smcarz = Factor("smcarz", ["sjui", "ikecv"])
khud = Factor("khud", ["bqht", "weiurp"])
def wdoday (khud, vsjz):
    return khud == vsjz
def xcf (khud, vsjz):
    return not wdoday(khud, vsjz)
zwizsh = Factor("zwizsh", [DerivedLevel("inny", WithinTrial(wdoday, [khud, vsjz])), DerivedLevel("foini", WithinTrial(xcf, [khud, vsjz]))])
design=[zwizsh,vsjz,jko,smcarz,khud]
constraints=[]
crossing=[smcarz,khud]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_1_0"))
