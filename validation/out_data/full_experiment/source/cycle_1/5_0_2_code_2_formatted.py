### REGULAR FACTORS
kbj = Factor("kbj", ["jnhscz", "enmgky"])
npycyx = Factor("npycyx", ["xbz", "pjtbin"])
ltjqdz = Factor("ltjqdz", ["jnhscz", "enmgky"])
dbb = Factor("dbb", ["xbz", "pjtbin"])
tdpseh = Factor("tdpseh", ["zgn", "sfu"])
### EXPERIMENT
constraints = [AtLeastKInARow(3, tdpseh), MinimumTrials(26)]
crossing = [npycyx, tdpseh]
design=[kbj,npycyx,ltjqdz,dbb,tdpseh]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
