from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
enPnCa_k=['cQBpBE[s',Level('lXSSSdp',1),')Bgv?4U@',"mWvKs",Level("UUUSnRt",2),"0Gw","?~funMrkJeN8",'h4myF6nA',';g;wRRu','UmKsYV8%']
FbQYFN=Factor("igTjkO",enPnCa_k)

### EXPERIMENT
design=[FbQYFN]
crossing=[FbQYFN]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/10_1_0"))
### END