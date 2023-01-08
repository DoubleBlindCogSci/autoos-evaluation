from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
lvylg = Factor("lvylg", ["atheg", "irduf"])
qlzbh = Factor("qlzbh", ["jstxk", "tlmmco"])
dcoqy = Factor("dcoqy", ["atheg", "irduf"])
zvfx = Factor("zvfx", ["jstxk", "tlmmco"])
vord = Factor("vord", ["qomtek", "lniqwx"])
lnvgik = Factor("lnvgik", ["cbal", "itukx"])
design=[lvylg,qlzbh,dcoqy,zvfx,vord,lnvgik]
constraints=[AtLeastKInARow(3, lvylg)]
crossing=[dcoqy,lvylg]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_0_1"))
