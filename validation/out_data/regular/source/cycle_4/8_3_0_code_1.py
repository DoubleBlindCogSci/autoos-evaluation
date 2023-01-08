from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qilQGuEz="Mt<kW"
WcXkO_vcB_=['DtolflCM5fYCAH',"QPS2N",'4|w','vYf:','seJSMA%]f',qilQGuEz,Level(')CSgqmV:',4),'nmba','a6brMZG']
tePmiXs447W=Factor("TZ3xjZ",WcXkO_vcB_)
E7FzKS=Factor('8R6cXdnjV#X',['GW|aFAYOPC',"SYiCIPX","bow",'YVjSmyWA',Level('GWmycbs|iLn',3),"iKkfMFi{",'OTZRBVtp',']Gp;a'])
CrNUoOi=Factor('MmlzVP}o',['hUNKjllG<UP2Gb'," QgeiT7CLEEh","2ygr ZjMz&_DJ","ZgA&CIRN",'!TUHih','Amsfx<LUOm',"y:Q",'QbtPzLZ|['])

### EXPERIMENT
design=[tePmiXs447W,E7FzKS,CrNUoOi]
crossing=[tePmiXs447W,E7FzKS,CrNUoOi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_3_0"))
### END