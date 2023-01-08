from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qynjdf = Factor("qynjdf", ["fivb", "ledy"])
sjdzy = Factor("sjdzy", ["vgdc", "tkqah"])
vppj = Factor("vppj", ["snlc", "dcz"])
tspx = Factor("tspx", ["oylqj", "eig"])
armh = Factor("armh", ["vjpiyd", "mel"])
pckl = Factor("pckl", ["godmhm", "nwat"])
kxqwj = Factor("kxqwj", ["kwikrb", "fhirpl"])
nnj = Factor("nnj", ["xiszlu", "sdd"])
tajrj = Factor("tajrj", ["qaeiei", "qjso"])
gihrlk = Factor("gihrlk", ["qtqwl", "kdo"])
cal = Factor("cal", ["uokf", "dsdo"])
eig = Factor("eig", ["jtmxs", "fsl"])
fro = Factor("fro", ["mokh", "anhek"])

### EXPERIMENT
design=[qynjdf,sjdzy,vppj,tspx,armh,pckl,kxqwj,nnj,tajrj,gihrlk,cal,eig,fro]
crossing=[[qynjdf,sjdzy,vppj,tspx],[armh],[pckl,kxqwj,nnj,tajrj],[gihrlk,cal,eig,fro],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_4"))
### END