### REGULAR FACTORS
mogppw = Factor("mogppw", ["nsmj", "hbav"])
ygz = Factor("ygz", ["lloiv", "epic"])
jxmg = Factor("jxmg", ["nsmj", "hbav"])
zuxak = Factor("zuxak", ["lloiv", "epic"])
imj = Factor("imj", ["pkq", "aeiu"])
### DERIVED FACTORS
##
def is_iaf_pgzwhl(zuxak, ygz):
    return zuxak == ygz
def is_iaf_acco(zuxak, ygz):
    return not is_iaf_pgzwhl(zuxak, ygz)
iaf= Factor("iaf", [DerivedLevel("pgzwhl", WithinTrial(is_iaf_pgzwhl, [zuxak, ygz])), DerivedLevel("acco", WithinTrial(is_iaf_acco, [zuxak, ygz]))])
### EXPERIMENT
constraints = [MinimumTrials(27), ExactlyK(4, (mogppw, "nsmj"))]
crossing = [jxmg, zuxak]
design=[mogppw,ygz,jxmg,zuxak,imj]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
