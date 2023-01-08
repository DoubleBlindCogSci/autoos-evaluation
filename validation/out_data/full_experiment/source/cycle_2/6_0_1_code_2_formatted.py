### REGULAR FACTORS
bmmkoy = Factor("bmmkoy", ["fbdy", "oobt"])
txl = Factor("txl", ["iato", "wmmzjh"])
tofpnu = Factor("tofpnu", ["fbdy", "oobt"])
xxegfy = Factor("xxegfy", ["iato", "wmmzjh"])
wha = Factor("wha", ["npf", "adl"])
vsmn = Factor("vsmn", ["qdj", "fppmhw"])
### EXPERIMENT
constraints = [AtMostKInARow(3, wha)]
crossing = [tofpnu, vsmn]
design=[bmmkoy,txl,tofpnu,xxegfy,wha,vsmn]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
