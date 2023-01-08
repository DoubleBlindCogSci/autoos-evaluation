### REGULAR FACTORS
toll = Factor("toll", ["nqwgeu", "wwudy"])
pkkm = Factor("pkkm", ["khun", "bkyhp"])
hhizte = Factor("hhizte", ["nqwgeu", "wwudy"])
rhl = Factor("rhl", ["khun", "bkyhp"])
### DERIVED FACTORS
##
def bpae (rhl, hhizte):
    return rhl == hhizte
def ygh (rhl, hhizte):
    return not bpae(rhl, hhizte)
cwh = Factor("cwh", [DerivedLevel("zdljt", WithinTrial(bpae, [rhl, hhizte])), DerivedLevel("blukz", WithinTrial(ygh, [rhl, hhizte]))])
##
def lfaj (pkkm, toll):
    return pkkm == toll
def sml (pkkm, toll):
    return not lfaj(pkkm, toll)
hnt = Factor("hnt", [DerivedLevel("rjvf", WithinTrial(lfaj, [pkkm, toll])), DerivedLevel("qoemb", WithinTrial(sml, [pkkm, toll]))])
### EXPERIMENT
design=[cwh,hnt,toll,pkkm,hhizte,rhl]
constraints=[MinimumTrials(36),AtLeastKInARow(4, hhizte)]
crossing=[toll,hhizte]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
