### REGULAR FACTORS
wisd = Factor("wisd", ["vzxi", "oqw"])
ufvgm = Factor("ufvgm", ["wlnkit", "ykhfb"])
uhi = Factor("uhi", ["vzxi", "oqw"])
qkblr = Factor("qkblr", ["wlnkit", "ykhfb"])
yztd = Factor("yztd", ["rofop", "hmrh"])
uybw = Factor("uybw", ["anliv", "rgvgo"])
### EXPERIMENT
constraints = [ExactlyK(2, (uybw, "anliv")), AtLeastKInARow(4, (ufvgm, "wlnkit"))]
crossing = [uhi, yztd]
design=[wisd,ufvgm,uhi,qkblr,yztd,uybw]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
