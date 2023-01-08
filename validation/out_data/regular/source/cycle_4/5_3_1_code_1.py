from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aj23=Factor("H]3Gy",["McJ","YE0EljDOS8<b","fJN^j","an]h",'pxgSXj'])
mvPqr9=">niF"
hRnfCZCK1=Factor("gzSpe2rw(PJ",["kpCRry",mvPqr9,"KiJnnEXa",'dHvgkVbBzCA',Level("g6ZRiFTYaj^(",2),"HRsG>lTDj"])
GkfwI39fD=["BlMPCuo","FzIRczt","GmTEPBKPmI","YYsI",Level('MaXKUTYqmV1B~j',1)]
RG4QtmNLXm=Factor("IIL~qDzfFREA",GkfwI39fD)

### EXPERIMENT
design=[aj23,hRnfCZCK1,RG4QtmNLXm]
crossing=[aj23,hRnfCZCK1,RG4QtmNLXm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3_1"))
### END