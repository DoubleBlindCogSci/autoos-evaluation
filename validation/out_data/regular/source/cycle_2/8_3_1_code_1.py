from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RnXex=Factor("xwQGDVF",["Uko",'gO4iSNuT',Level("lRxrEeOEoIY",1),"&dVwiX",Level('mpM',4),Level("7lsu7Dsxp7ZsB",9),Level("NVwN",9),Level('8lqI;VSlnF!yK',4)])
YlA4Xus4=Level('yQbe!q}OuE;',8)
cuB6Dtq_41A=Level("yLC6wmxzi",4)
Qxusi1e8R4=Factor('iRabLm7ssv',[cuB6Dtq_41A,'pCw',"oVH3Mg|JwHrf",Level('klZF:YoOMK',3),'JDMNj',YlA4Xus4,Level("O:stSVaCELg",2),"drzYtM","uzY&NM Ts",Level('WZcPjpRX7ZB',7)])
Rj8IHi=Factor("ER vn99FM",['SOOR','hfDb8oO',Level("zxiBZ",10),"cJqEzja",'EQPbrTar%','fBizdUpK',Level('BuqtjEHrfD',9),"pKH"])

### EXPERIMENT
design=[RnXex,Qxusi1e8R4,Rj8IHi]
crossing=[RnXex,Qxusi1e8R4,Rj8IHi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_3_1"))
### END