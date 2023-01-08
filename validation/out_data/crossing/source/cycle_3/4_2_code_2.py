from sweetpea import *
import os
_dir=os.path.dirname(__file__)
qrb = Factor("qrb", ["xmtxcu", "cizamj"])
xwscf = Factor("xwscf", ["ngub", "ljl"])
lvjonx = Factor("lvjonx", ["vgsw", "pnf"])
asnc = Factor("asnc", ["ynvzu", "jsl"])
vivr = Factor("vivr", ["zvgmw", "lab"])
qlaijq = Factor("qlaijq", ["ndxln", "sgkm"])
hovzo = Factor("hovzo", ["ntsk", "hltpm"])
udek = Factor("udek", ["irz", "yttx"])
vztuzg = Factor("vztuzg", ["qqiyjm", "harqsn"])
constraints = []
crossing = [[qrb, xwscf, lvjonx, asnc], [vivr, qlaijq, hovzo, udek, vztuzg]]


design=[qrb,xwscf,lvjonx,asnc,vivr,qlaijq,hovzo,udek,vztuzg]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2"))

### END