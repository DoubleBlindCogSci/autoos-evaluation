### REGULAR FACTORS
wisd = Factor("wisd", ["vzxi", "oqw"])
ufvgm = Factor("ufvgm", ["wlnkit", "ykhfb"])
uhi = Factor("uhi", ["vzxi", "oqw"])
qkblr = Factor("qkblr", ["wlnkit", "ykhfb"])
yztd = Factor("yztd", ["rofop", "hmrh"])
uybw = Factor("uybw", ["anliv", "rgvgo"])
### EXPERIMENT
design=[wisd,ufvgm,uhi,qkblr,yztd,uybw]
constraints=[ExactlyKInARow(2, uybw),AtLeastKInARow(4, ufvgm)]
crossing=[uhi,yztd]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
