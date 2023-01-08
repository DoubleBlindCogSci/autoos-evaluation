### REGULAR FACTORS
kbj = Factor("kbj", ["jnhscz", "enmgky"])
npycyx = Factor("npycyx", ["xbz", "pjtbin"])
ltjqdz = Factor("ltjqdz", ["jnhscz", "enmgky"])
dbb = Factor("dbb", ["xbz", "pjtbin"])
tdpseh = Factor("tdpseh", ["zgn", "sfu"])
### EXPERIMENT
design=[kbj,npycyx,ltjqdz,dbb,tdpseh]
constraints=[AtLeastKInARow(3, tdpseh),MinimumTrials(26)]
crossing=[npycyx,tdpseh]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
