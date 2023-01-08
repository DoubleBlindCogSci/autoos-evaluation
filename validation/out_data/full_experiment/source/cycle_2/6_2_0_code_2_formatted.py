### REGULAR FACTORS
engo = Factor("engo", ["lbjuv", "dyo"])
kctkp = Factor("kctkp", ["izl", "rgaqux"])
vnp = Factor("vnp", ["lbjuv", "dyo"])
qid = Factor("qid", ["izl", "rgaqux"])
itpxp = Factor("itpxp", ["jpnqdt", "uai"])
gxh = Factor("gxh", ["gbrd", "ncogvs"])
### DERIVED FACTORS
##
def is_jfvhy_gqppy(vnp, gxh):
    return vnp == gxh
def is_jfvhy_nyza(vnp, gxh):
    return not is_jfvhy_gqppy(vnp, gxh)
jfvhy= Factor("jfvhy", [DerivedLevel("gqppy", WithinTrial(is_jfvhy_gqppy, [vnp, gxh])), DerivedLevel("nyza", WithinTrial(is_jfvhy_nyza, [vnp, gxh]))])
##
def is_oclt_vbw(engo, qid):
    return engo == qid
def is_oclt_qqz(engo, qid):
    return not is_oclt_vbw(engo, qid)
oclt= Factor("oclt", [DerivedLevel("vbw", WithinTrial(is_oclt_vbw, [engo, qid])), DerivedLevel("qqz", WithinTrial(is_oclt_qqz, [engo, qid]))])
### EXPERIMENT
constraints = []
crossing = [jfvhy, itpxp]
design=[engo,kctkp,vnp,qid,itpxp,gxh]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
