from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Mxdqx_9Ws=Level("osUdJB&Edxl",4)
Z1MUEw0Cisl=Factor("eIRV%I",[Mxdqx_9Ws,"hAimCiOE","XbB^LaV","pRW3HNV4FkK","lo@vVSx","!bPl:LIiQzwukG",'#DzQ3'])
VJblWGDK=Factor('Fxz$Uob?boxm1b',["&uypFVf",'IfOKO|',"~6ZvX*Hl|VI7NJ","vdQPuaKTdc","vMshw[HSHoJJhZ","pqFGMs<"])
KkK1SyE4R='XTb1X~ZLlgEe'
goOyC7c5Om=Factor("EwaZ&gw;b4",[Level('oRyp',4),'WQknLrt','zwlTSd',"nD en:WCYHa6d",'~wdw',Level('|CUWyxo',1),KkK1SyE4R])

### EXPERIMENT
design=[Z1MUEw0Cisl,VJblWGDK,goOyC7c5Om]
crossing=[Z1MUEw0Cisl,VJblWGDK,goOyC7c5Om]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3_0"))
### END