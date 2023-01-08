from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
YEzsA="j<QkW"
irsl1mvBinz=Factor("N6Bn",[Level("Ldm",4),'chrUvnM|ZQvCS',YEzsA,">4lT7",'vZHr','K2ghss<YwE[Q','Y8aTbwKWnph',Level("mrJ",9)])
wTaEYf7bF=' pUWH'
ytWI0=Factor("hfm_3",[Level('fsEF',6),wTaEYf7bF,Level("OTUOppP;VCi",3),"hdurS",Level('ISuXvoVCPDP',9),Level("Qu2",2),'#K#F}dLXUh&RI',"WFKa"])
ErC0q="MFdi8MQhP[G"
MSXaO8=Factor("uPdZ<ygZP",[ErC0q,'UijZHGvx',Level("fltZe^8IxXIR",2),'b(b7OhdQPuFKE','HOX6XppTGg','saLs{Ze8Bu$ ',"os>jNIjMK","8SOhj[hhC"])

### EXPERIMENT
design=[irsl1mvBinz,ytWI0,MSXaO8]
crossing=[irsl1mvBinz,ytWI0,MSXaO8]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3_0"))
### END