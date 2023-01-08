### REGULAR FACTORS
lvylg = Factor("lvylg", ["atheg", "irduf"])
qlzbh = Factor("qlzbh", ["jstxk", "tlmmco"])
dcoqy = Factor("dcoqy", ["atheg", "irduf"])
zvfx = Factor("zvfx", ["jstxk", "tlmmco"])
vord = Factor("vord", ["qomtek", "lniqwx"])
lnvgik = Factor("lnvgik", ["cbal", "itukx"])
### EXPERIMENT
design=[lvylg,qlzbh,dcoqy,zvfx,vord,lnvgik]
constraints=[AtLeastKInARow(3, lvylg)]
crossing=[dcoqy,lvylg]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
