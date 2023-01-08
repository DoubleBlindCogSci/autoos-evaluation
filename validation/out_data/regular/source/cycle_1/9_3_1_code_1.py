from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DGEJ2HR4H=Factor("aCxZeoeIL3juMW",["AxszFnNWuiI",'eweZMTbkNOD^',Level("u?v_KojSN|WPkS",4),Level('v)StcoGOF',3),"dFcgB","gHPSg",Level('Lq?FQcPOtb0nWj',4),'QWNm','gqeq'])
nxKHGQ1aeq=Factor('Yvxqae',['NkTvHpRSBqz',Level(":@C tggT>F0)NH",7),"Btt7",Level("NLsPUZqahHqnL",1),Level("vZom[QL",2),Level("ZMyqTbglCTDi0",2),"tkT$FZJ",'JLX)','Bdm'])
AskoRG="IfWH!xcHsJK"
TUfDA8n=Factor('mEpmn;lMKd?',[Level("TxWoCsPHzHTAV",3),'b6lkWxOWN',Level('RYY!oBjzT[qy',5),'|ZPSx1L',"0jeea","9ZiOey7","q WNxi:F[BY","L6qqLLzMeAuz","SoZ",AskoRG])

### EXPERIMENT
design=[DGEJ2HR4H,nxKHGQ1aeq,TUfDA8n]
crossing=[DGEJ2HR4H,nxKHGQ1aeq,TUfDA8n]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/9_3_1"))
### END