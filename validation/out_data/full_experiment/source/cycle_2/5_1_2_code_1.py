from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
mogppw = Factor("mogppw", ["nsmj", "hbav"])
ygz = Factor("ygz", ["lloiv", "epic"])
jxmg = Factor("jxmg", ["nsmj", "hbav"])
zuxak = Factor("zuxak", ["lloiv", "epic"])
imj = Factor("imj", ["pkq", "aeiu"])
def djklo (zuxak, ygz):
    return zuxak == ygz
def prmecd (zuxak, ygz):
    return not djklo(zuxak, ygz)
iaf = Factor("iaf", [DerivedLevel("pgzwhl", WithinTrial(djklo, [zuxak, ygz])), DerivedLevel("acco", WithinTrial(prmecd, [zuxak, ygz]))])
design=[iaf,mogppw,ygz,jxmg,zuxak,imj]
constraints=[ExactlyKInARow(4, mogppw),MinimumTrials(27)]
crossing=[jxmg,zuxak]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_2"))
