### REGULAR FACTORS
vrern = Factor("vrern", ["ofdjhs", "ansm"])
nfi = Factor("nfi", ["ofxmh", "lyvsf"])
esewp = Factor("esewp", ["ofdjhs", "ansm"])
ffr = Factor("ffr", ["ofxmh", "lyvsf"])
### EXPERIMENT
constraints=[AtMostKInARow(3, esewp),AtLeastKInARow(4, ffr)]
crossing=[ffr,esewp]
design=[vrern,nfi,esewp,ffr]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
