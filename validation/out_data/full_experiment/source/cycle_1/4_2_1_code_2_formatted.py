### REGULAR FACTORS
zzdmwj = Factor("zzdmwj", ["ioetr", "jlbmqt"])
gkn = Factor("gkn", ["ocdj", "ovk"])
evz = Factor("evz", ["ioetr", "jlbmqt"])
toiht = Factor("toiht", ["ocdj", "ovk"])
### DERIVED FACTORS
##
def is_khvnl_kknbk(evz, zzdmwj):
    return evz == zzdmwj
def is_khvnl_gebdr(evz, zzdmwj):
    return not is_khvnl_kknbk(evz, zzdmwj)
khvnl= Factor("khvnl", [DerivedLevel("kknbk", WithinTrial(is_khvnl_kknbk, [evz, zzdmwj])), DerivedLevel("gebdr", WithinTrial(is_khvnl_gebdr, [evz, zzdmwj]))])
##
def is_fdan_cjjghi(gkn, toiht):
    return gkn == toiht
def is_fdan_urts(gkn, toiht):
    return not is_fdan_cjjghi(gkn, toiht)
fdan= Factor("fdan", [DerivedLevel("cjjghi", WithinTrial(is_fdan_cjjghi, [gkn, toiht])), DerivedLevel("urts", WithinTrial(is_fdan_urts, [gkn, toiht]))])
### EXPERIMENT
constraints = [AtLeastKInARow(2, (evz, "ioetr"))]
crossing = [khvnl, gkn]
design=[zzdmwj,gkn,evz,toiht,khvnl,fdan]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
