from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
WUWwS2sGkG=Factor('IFianaRLFw',["3lIxCbWtjU@aeK",'}G8%!p',"eYHU",'EXHIiw(myce',"ig8rwTRloZn",Level('dBGyaZKn 1I]vG',4),"t(E8iu"])
LvzzL_=['ZAr',"Kv9Z9kW",'s!}U',Level("VmWdiT",9),Level('QHesrX&5XnU',1),'m1wUnTbe']
j6oAUeNZRi=['DUz ucY1na','Zgog',"USMSw2g^Inr","GI]bN6"]
SFvE0hf=Factor("PGxfqfvHjV{",[j6oAUeNZRi[0],"fnJFR","]RMPX9sY{vQDm",'sS@Y','qDVMv',LvzzL_[1],'DlQG$LlMyh(f',"CIYBliC",Level('Mw@|qRC~z',8)])

### EXPERIMENT
design=[WUWwS2sGkG,SFvE0hf]
crossing=[WUWwS2sGkG,SFvE0hf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/7_2_0"))
### END