from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
wisd = Factor("wisd", ["vzxi", "oqw"])
ufvgm = Factor("ufvgm", ["wlnkit", "ykhfb"])
uhi = Factor("uhi", ["vzxi", "oqw"])
qkblr = Factor("qkblr", ["wlnkit", "ykhfb"])
yztd = Factor("yztd", ["rofop", "hmrh"])
uybw = Factor("uybw", ["anliv", "rgvgo"])
design=[wisd,ufvgm,uhi,qkblr,yztd,uybw]
constraints=[ExactlyKInARow(2, uybw),AtLeastKInARow(4, ufvgm)]
crossing=[uhi,yztd]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_0_2"))
