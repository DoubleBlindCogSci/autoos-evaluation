from sweetpea import *
import os
_dir=os.path.dirname(__file__)
mwl = Factor("mwl", ["yrk", "ftmsmd"])
wxrk = Factor("wxrk", ["zxpc", "zhd"])
vwlfs = Factor("vwlfs", ["srr", "uls"])
jxmneh = Factor("jxmneh", ["jgdtte", "trd"])
lwimrr = Factor("lwimrr", ["edykcg", "sbved"])
qmyt = Factor("qmyt", ["imqo", "lyqxsn"])
rhb = Factor("rhb", ["qurmxf", "rghx"])
fyywz = Factor("fyywz", ["zztcep", "zkmpl"])
wtwqze = Factor("wtwqze", ["yxtxif", "fqxuy"])
ijzprx = Factor("ijzprx", ["yyh", "nas"])
ghk = Factor("ghk", ["rayzdp", "ojv"])
constraints = []
crossing = [[mwl, wxrk, vwlfs], [jxmneh, lwimrr, qmyt, rhb], [fyywz, wtwqze, ijzprx], [ghk]]


design=[mwl,wxrk,vwlfs,jxmneh,lwimrr,qmyt,rhb,fyywz,wtwqze,ijzprx,ghk]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_5"))

### END