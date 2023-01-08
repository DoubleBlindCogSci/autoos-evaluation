from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
wxkp = Factor("wxkp", ["iqsqug", "ygc"])
fgiigi = Factor("fgiigi", ["ukk", "nojgu"])
vmp = Factor("vmp", ["iqsqug", "ygc"])
fzb = Factor("fzb", ["ukk", "nojgu"])
kpdy = Factor("kpdy", ["hkoia", "mploi"])
def is_gdzodz_mwod(vmp, fzb):
    return vmp == fzb
def is_gdzodz_blf(vmp, fzb):
    return not is_gdzodz_mwod(vmp, fzb)
gdzodz = Factor("gdzodz", [DerivedLevel("mwod", WithinTrial(is_gdzodz_mwod, [vmp, fzb])), DerivedLevel("blf", WithinTrial(is_gdzodz_blf, [vmp, fzb]))])
def is_bbo_dxh(fgiigi, wxkp):
    return fgiigi == wxkp
def is_bbo_hox(fgiigi, wxkp):
    return not is_bbo_dxh(fgiigi, wxkp)
bbo = Factor("bbo", [DerivedLevel("dxh", WithinTrial(is_bbo_dxh, [fgiigi, wxkp])), DerivedLevel("hox", WithinTrial(is_bbo_hox, [fgiigi, wxkp]))])
constraints = [AtMostKInARow(2, fgiigi), AtLeastKInARow(3, gdzodz)]
crossing = [fzb, gdzodz]

design=[wxkp,fgiigi,vmp,fzb,kpdy,gdzodz,bbo]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_2"))
