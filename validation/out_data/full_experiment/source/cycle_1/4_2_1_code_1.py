from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
zzdmwj = Factor("zzdmwj", ["ioetr", "jlbmqt"])
gkn = Factor("gkn", ["ocdj", "ovk"])
evz = Factor("evz", ["ioetr", "jlbmqt"])
toiht = Factor("toiht", ["ocdj", "ovk"])
def etfev (evz, zzdmwj):
    return evz == zzdmwj
def vea (evz, zzdmwj):
    return not etfev(evz, zzdmwj)
khvnl = Factor("khvnl", [DerivedLevel("kknbk", WithinTrial(etfev, [evz, zzdmwj])), DerivedLevel("gebdr", WithinTrial(vea, [evz, zzdmwj]))])
def doyx (gkn, toiht):
    return gkn == toiht
def pgesuj (gkn, toiht):
    return not doyx(gkn, toiht)
fdan = Factor("fdan", [DerivedLevel("cjjghi", WithinTrial(doyx, [gkn, toiht])), DerivedLevel("urts", WithinTrial(pgesuj, [gkn, toiht]))])
design=[khvnl,fdan,zzdmwj,gkn,evz,toiht]
constraints=[AtLeastKInARow(2, evz)]
crossing=[khvnl,gkn]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_2_1"))
