### REGULAR FACTORS
wtmrd = Factor("wtmrd", ["ubkei", "emek"])
jqvsip = Factor("jqvsip", ["hziva", "tklmk"])
pvzxug = Factor("pvzxug", ["ubkei", "emek"])
hrycmu = Factor("hrycmu", ["hziva", "tklmk"])
bpf = Factor("bpf", ["wimnk", "vdearw"])
### EXPERIMENT
design=[wtmrd,jqvsip,pvzxug,hrycmu,bpf]
constraints=[]
crossing=[wtmrd,bpf]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
