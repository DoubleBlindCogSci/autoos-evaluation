### REGULAR FACTORS
wxkp = Factor("wxkp", ["iqsqug", "ygc"])
fgiigi = Factor("fgiigi", ["ukk", "nojgu"])
vmp = Factor("vmp", ["iqsqug", "ygc"])
fzb = Factor("fzb", ["ukk", "nojgu"])
kpdy = Factor("kpdy", ["hkoia", "mploi"])
### DERIVED FACTORS
##
def is_gdzodz_mwod(vmp, fzb):
    return vmp == fzb
def is_gdzodz_blf(vmp, fzb):
    return not is_gdzodz_mwod(vmp, fzb)
gdzodz = Factor("gdzodz", [DerivedLevel("mwod", WithinTrial(is_gdzodz_mwod, [vmp, fzb])), DerivedLevel("blf", WithinTrial(is_gdzodz_blf, [vmp, fzb]))])
##
def is_bbo_dxh(fgiigi, wxkp):
    return fgiigi == wxkp
def is_bbo_hox(fgiigi, wxkp):
    return not is_bbo_dxh(fgiigi, wxkp)
bbo = Factor("bbo", [DerivedLevel("dxh", WithinTrial(is_bbo_dxh, [fgiigi, wxkp])), DerivedLevel("hox", WithinTrial(is_bbo_hox, [fgiigi, wxkp]))])
### EXPERIMENT
constraints = [AtMostKInARow(2, fgiigi), AtLeastKInARow(3, gdzodz)]
crossing = [fzb, gdzodz]
design=[wxkp,fgiigi,vmp,fzb,kpdy,gdzodz,bbo]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
