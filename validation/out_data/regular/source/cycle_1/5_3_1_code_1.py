from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qxVy48N0lw=Factor('hDgQWaXpJJ6Z',["Zqh)C1x",Level('mt]IDVYR@UZH',9),'fMKmyzbf','DELscRU#P|utl}','fC>DXcdXJQMjhm'])
gwa26ZWKC=Level("SNL",9)
df5WDh9McCW=Factor('wGgWr',[gwa26ZWKC,Level("FSH",1),"cxlmR",Level("enWvs]SdPQfU",2),Level('FMyr_g3lEfn',10),'pXBiAxc|'])
VmOWCt3=Factor("ynYzCPvL%mPs",['dQstz?fp)Um','CziVPGnK','Kpt',Level("kyhQSeMg",4),"jtcK"])

### EXPERIMENT
design=[qxVy48N0lw,df5WDh9McCW,VmOWCt3]
crossing=[qxVy48N0lw,df5WDh9McCW,VmOWCt3]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_3_1"))
### END