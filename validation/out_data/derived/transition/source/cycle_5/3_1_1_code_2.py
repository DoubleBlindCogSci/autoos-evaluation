from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uano = Factor("uano", ["hspapo","hlyj","swp","motz","okbuz","scxcn"])
def is_zzbnv_szyjh(uano):
    return uano[0] == "hspapo" and uano[-1] != "okbuz"
def is_zzbnv_xogpak(uano):
    return uano[0] != "hspapo" and uano[-1] == "okbuz"
def is_zzbnv_fkkgx(uano):
    return not (is_zzbnv_szyjh(uano) or is_zzbnv_xogpak(uano))
zzbnv = Factor("zzbnv", [DerivedLevel("szyjh", Transition(is_zzbnv_szyjh, [uano])), DerivedLevel("xogpak", Transition(is_zzbnv_xogpak, [uano])), DerivedLevel("fkkgx", Transition(is_zzbnv_fkkgx, [uano]))])

design=[uano,zzbnv]
crossing=[zzbnv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END