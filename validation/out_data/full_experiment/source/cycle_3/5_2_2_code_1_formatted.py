### REGULAR FACTORS
wxkp = Factor("wxkp", ["iqsqug", "ygc"])
fgiigi = Factor("fgiigi", ["ukk", "nojgu"])
vmp = Factor("vmp", ["iqsqug", "ygc"])
fzb = Factor("fzb", ["ukk", "nojgu"])
kpdy = Factor("kpdy", ["hkoia", "mploi"])
### DERIVED FACTORS
##
def smgg (vmp, fzb):
    return vmp == fzb
def xskmy (vmp, fzb):
    return not smgg(vmp, fzb)
gdzodz = Factor("gdzodz", [DerivedLevel("mwod", WithinTrial(smgg, [vmp, fzb])), DerivedLevel("blf", WithinTrial(xskmy, [vmp, fzb]))])
##
def fdl (fgiigi, wxkp):
    return fgiigi == wxkp
def hgw (fgiigi, wxkp):
    return not fdl(fgiigi, wxkp)
bbo = Factor("bbo", [DerivedLevel("dxh", WithinTrial(fdl, [fgiigi, wxkp])), DerivedLevel("hox", WithinTrial(hgw, [fgiigi, wxkp]))])
### EXPERIMENT
design=[gdzodz,bbo,wxkp,fgiigi,vmp,fzb,kpdy]
constraints=[AtMostKInARow(2, fgiigi),AtLeastKInARow(3, gdzodz)]
crossing=[fzb,gdzodz]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
