from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
mogppw = Factor("mogppw", ["nsmj", "hbav"])
ygz = Factor("ygz", ["lloiv", "epic"])
jxmg = Factor("jxmg", ["nsmj", "hbav"])
zuxak = Factor("zuxak", ["lloiv", "epic"])
imj = Factor("imj", ["pkq", "aeiu"])
def is_iaf_pgzwhl(zuxak, ygz):
    return zuxak == ygz
def is_iaf_acco(zuxak, ygz):
    return not is_iaf_pgzwhl(zuxak, ygz)
iaf= Factor("iaf", [DerivedLevel("pgzwhl", WithinTrial(is_iaf_pgzwhl, [zuxak, ygz])), DerivedLevel("acco", WithinTrial(is_iaf_acco, [zuxak, ygz]))])
constraints = [MinimumTrials(27), ExactlyK(4, (mogppw, "nsmj"))]
crossing = [jxmg, zuxak]

design=[mogppw,ygz,jxmg,zuxak,imj,iaf]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_2"))
