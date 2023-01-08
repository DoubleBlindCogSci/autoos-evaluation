from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mfz= Factor("mfz", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
jtrvnd= Factor("jtrvnd", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
zrs= Factor("zrs", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
def is_yaehve_rap(zrs, mfz, jtrvnd):
    return zrs[0] == mfz[-1]
def is_yaehve_gpksp(zrs, mfz, jtrvnd):
    return zrs[0] != mfz[-1] and jtrvnd[0] == mfz[-2]
def is_yaehve_xqjhvf(zrs, mfz, jtrvnd):
    return not (is_yaehve_rap(zrs, mfz, jtrvnd) or is_yaehve_gpksp(zrs, mfz, jtrvnd))
yaehve= Factor("yaehve", [DerivedLevel("rap", Window(is_yaehve_rap, [zrs, mfz, jtrvnd], 3, 1)), DerivedLevel("gpksp", Window(is_yaehve_gpksp, [zrs, mfz, jtrvnd], 3, 1)), DerivedLevel("xqjhvf", Window(is_yaehve_xqjhvf, [zrs, mfz, jtrvnd], 3, 1))])

design=[mfz,jtrvnd,zrs,yaehve]
crossing=[yaehve]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
