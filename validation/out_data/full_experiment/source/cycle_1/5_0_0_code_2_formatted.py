### REGULAR FACTORS
wtmrd = Factor("wtmrd", ["ubkei", "emek"])
jqvsip = Factor("jqvsip", ["hziva", "tklmk"])
pvzxug = Factor("pvzxug", ["ubkei", "emek"])
hrycmu = Factor("hrycmu", ["hziva", "tklmk"])
bpf = Factor("bpf", ["wimnk", "vdearw"])
### EXPERIMENT
constraints = []
crossing = [wtmrd, bpf]
design=[wtmrd,jqvsip,pvzxug,hrycmu,bpf]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
