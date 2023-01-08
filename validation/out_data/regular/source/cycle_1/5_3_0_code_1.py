from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
biQo8=Factor("JPEeK bkk",['xekdk!qo1KXd',"uoRn",']s;LlOhKDh4nO',Level('dg[KbbqeYb',6),'JOPDSRc'])
SUTxR=Factor("FYdEXnj_hvR0",[Level("lvOntGk",3),'rPHWnDpjUUj','yOX ',"w4Hraly8rOCOt","Jplf&syKU"])
DbAo=[')oBbh(daJ6KS3','KeLIpuG GlY','UO>aKUuZXspP)F']
nWbupQoiJMW=Factor('AmUdvwcYmOEu',[Level('^ucgbDZUF8',1),Level('Wax*Rn',6),"jPrdx3>eh","LCxxI[gA",Level('g]DoKdSY',7),DbAo[2]])

### EXPERIMENT
design=[biQo8,SUTxR,nWbupQoiJMW]
crossing=[biQo8,SUTxR,nWbupQoiJMW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_3_0"))
### END