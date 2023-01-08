from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mapn = Factor("mapn", ["gatjmi", "pfuvnj"])
svn = Factor("svn", ["fyxdz", "dfcahi"])
rqn = Factor("rqn", ["qera", "enxv"])
dpj = Factor("dpj", ["ejjbvu", "oonq"])
ary = Factor("ary", ["flhsp", "mbofd"])
kfwexi = Factor("kfwexi", ["sht", "wskwx"])
hjaizc = Factor("hjaizc", ["mmssj", "hsqhn"])
qxxcli = Factor("qxxcli", ["vbauw", "ejgz"])
bgio = Factor("bgio", ["uaw", "atrjds"])
jjzp = Factor("jjzp", ["uth", "gzqxlx"])
xirvg = Factor("xirvg", ["qtzscj", "eogupy"])

### EXPERIMENT
design=[mapn,svn,rqn,dpj,ary,kfwexi,hjaizc,qxxcli,bgio,jjzp,xirvg]
crossing=[[mapn],[svn],[rqn,dpj,ary],[kfwexi,hjaizc,qxxcli],[bgio],[jjzp,xirvg],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2"))
### END