from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ClzxESGoy5=['F{DEHr!hkbu',"hwulG",Level("5fB",7),Level('g$Tw$|hD',4)]
WUsClyUxJ=Factor("QsiCS>NyiKOI",["u7SXgrVA","Hd6AZsP FXzpp","QvwsJ!LQQh^",ClzxESGoy5[3],Level('gkOA',8),"J91",'FyJIroW '])
qmgNRpFry=Factor("yVhWORI$ybTCAg",['qEFFZyBFt','[C8@TLkuV','NuvEuCcGONdo)',"ZWkLap&c|*","fG4JV","LKsyttOx#nmMW"])
LaQQ19=['cZEp<RcyYb3',Level('fAM',10),"cpthQgvUnDjnyW","nn^^Z0sUgEwJSs","4et","PPbXZyNzKamVf"]
OzNhfCyUQ9=Factor("wnyiy",["oOVc]WxP",LaQQ19[1],'mi}vqR8C[A',Level("D?vL*lPpIlXcoZ",6),Level('MtYptrglyal',4),"gUxcnoK",Level("#ozHPj%",2)])

### EXPERIMENT
design=[WUsClyUxJ,qmgNRpFry,OzNhfCyUQ9]
crossing=[WUsClyUxJ,qmgNRpFry,OzNhfCyUQ9]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3_1"))
### END