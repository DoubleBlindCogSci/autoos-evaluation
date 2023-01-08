from sweetpea import *
import os
_dir=os.path.dirname(__file__)
zsgb = Factor("zsgb", ["rwwo", "cacbck"])
slpkqw = Factor("slpkqw", ["sxbhy", "ahxg"])
ykb = Factor("ykb", ["oon", "elz"])
uizcuo = Factor("uizcuo", ["roppm", "hrxz"])
xtffon = Factor("xtffon", ["lij", "thxld"])
tzhx = Factor("tzhx", ["hng", "uikcof"])
tzypp = Factor("tzypp", ["dcdyuq", "dsc"])
zgrei = Factor("zgrei", ["gaffl", "pcqs"])
iurc = Factor("iurc", ["kwrr", "qmisd"])
mbwxg = Factor("mbwxg", ["wigm", "bvw"])
ziyw = Factor("ziyw", ["fwk", "myiqf"])
sqlj = Factor("sqlj", ["kscwp", "kqayzs"])
yavu = Factor("yavu", ["yfl", "scayz"])
constraints = []
crossing = [[zsgb, slpkqw], [ykb, uizcuo, xtffon, tzhx], [tzypp, zgrei, iurc, mbwxg], [ziyw, sqlj, yavu]]


design=[zsgb,slpkqw,ykb,uizcuo,xtffon,tzhx,tzypp,zgrei,iurc,mbwxg,ziyw,sqlj,yavu]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3"))

### END