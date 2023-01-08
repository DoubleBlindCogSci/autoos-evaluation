from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
xsoc = Factor("xsoc", ["aick", "thojyk"])
qzjdvx = Factor("qzjdvx", ["orlug", "condlo"])
syz = Factor("syz", ["aick", "thojyk"])
qgx = Factor("qgx", ["orlug", "condlo"])
oubi = Factor("oubi", ["rnje", "wawxwx"])
constraints = [AtLeastKInARow(2, qgx), ExactlyKInARow(2, qzjdvx)]
crossing = [qgx, syz]

design=[xsoc,qzjdvx,syz,qgx,oubi]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_0_2"))
