from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
xsoc = Factor("xsoc", ["aick", "thojyk"])
qzjdvx = Factor("qzjdvx", ["orlug", "condlo"])
syz = Factor("syz", ["aick", "thojyk"])
qgx = Factor("qgx", ["orlug", "condlo"])
oubi = Factor("oubi", ["rnje", "wawxwx"])
design=[xsoc,qzjdvx,syz,qgx,oubi]
constraints=[AtLeastKInARow(2, qgx),ExactlyKInARow(2, qzjdvx)]
crossing=[qgx,syz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_0_2"))
