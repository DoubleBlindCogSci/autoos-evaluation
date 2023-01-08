from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
MsM4pS=[Level("srKtJYiwZr",3),"JO>ZDvyCgvMJB","cXsT$KKwLdBq","KqrbIo8eEo"]
XKN7=Factor("NjgQFJ",MsM4pS)
t65iPUYr=Factor('OFbEmU',['wjZfj',"lsH","gqeazvclevrST","FnH"])
l39CNLL="PIQ9JkUoOyII"
F6P9oJysU=Factor('?82Q^&IGtfRfZ',['uIaKxy;ptAK',"DycIbXUYN",Level('SVi',3),'Cjc|{Dua z',l39CNLL])

### EXPERIMENT
design=[XKN7,t65iPUYr,F6P9oJysU]
crossing=[XKN7,t65iPUYr,F6P9oJysU]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3_0"))
### END