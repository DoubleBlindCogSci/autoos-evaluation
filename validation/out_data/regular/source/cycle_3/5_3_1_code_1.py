from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
X4gcOb=Factor('rywp9s)B;pNz',["ol1SNL>urpCs",'ToZiajcDY;L','U?HanBxlgxiyg','SnZvzhVuD','[ZSxI0yW '])
dcOwd6AU7a0='XcrrEEQ&dzWJ~'
ecf5=Level(" nd1 wXhC]^H",7)
CfA2j=Factor('D1ZpVNQD',[ecf5,"~sKt_K[|",Level("LQSA1zljHPc",2),dcOwd6AU7a0,Level('WcGk',9),Level('Yp(RKdbeg',6),'psxeRCdwbOqyo'])
u2hHDxYBX0=Factor('W<bOaSC',["[V&jJVtYY","qtW",'w{U^N2Y(G',"wFHo",'mSNIXej*eKdjKD'])

### EXPERIMENT
design=[X4gcOb,CfA2j,u2hHDxYBX0]
crossing=[X4gcOb,CfA2j,u2hHDxYBX0]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3_1"))
### END