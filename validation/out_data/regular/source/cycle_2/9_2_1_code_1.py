from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
TN_uzMuxLbZ=Factor('EURYH68',['SxYEA',"rGtQrRKtSF","pHEp)RWpyZ",Level('sMSo2F;!',8),'nx6GulJ','c{Oeo<QF','bON','vEMO {FwTRQH',"71s"])
uOFNi2=Level("0mjNr",5)
FzGJwhJqr=Factor('wX#^laii',[uOFNi2,"fPET",Level("Hb)",9),'yuJOaLEA',"o]jJ9g%MLYfZC",Level('TPNi2trc}hy',6),"lRsU6vwOQJa4","p6b$hq[A","*Lf|!Ft~zG3QF","hiEuuxnMoB7I"])

### EXPERIMENT
design=[TN_uzMuxLbZ,FzGJwhJqr]
crossing=[TN_uzMuxLbZ,FzGJwhJqr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_2_1"))
### END