from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oMYO_MLKoqNdZ = Factor("oMYO}MLKoqNdZ", ["oMhVhE", "h2pQyTw", "Sfb>qHF", "n6btJvN7Cx&ya"])

design=[oMYO_MLKoqNdZ]
crossing=[oMYO_MLKoqNdZ]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_1"))

### END
