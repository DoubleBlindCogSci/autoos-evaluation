from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZDXzy6L1vSx=Level('ShtIhkGJAUZ>c',10)
fIxqkOPpIY=Factor("0D{b~bxWrwQ[",["cEG|AN",'AxYZHAuaw:KhLA',"#ynLG<LYipZUi","WWJYaXjVdZjk{","gT (ibn|nvV",ZDXzy6L1vSx,"YD EuFMgoO",'RWcR[gfEw','AzRHf'])
c6YMgchMqv=["YDbPSaXjqFd(",Level("iwx",6),"vOb2$Yfyz5","5aZM<","GQmm?Gq",Level('vRPsA)vO#7z',10),Level("!vT",1),'KM:klJAhW|h']
g9P7bBki=Factor("?^i",c6YMgchMqv)

### EXPERIMENT
design=[fIxqkOPpIY,g9P7bBki]
crossing=[fIxqkOPpIY,g9P7bBki]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/8_2_1"))
### END