from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
atISnwmWtks = Factor("atISnwmWtks", ["QvV", "_rlRsmAg{Q", "IqQAAQL", "l^Lh[Bnhx"])
oO_XCRR = Factor("oO XCRR", [Level("0Jme", 1), Level("t@HHhyQevS", 1), Level("*ZCwL?{KQogs", 1), Level("FNDNa", 2), Level("Sx]uz~q4Nb", 1)])
IyVpmnqGLUUB = Factor("IyVpmnqGLUUB", [Level("BxKKPj;_gcUL", 3), Level(" ioqk", 1), Level("S]cvEsXQuTp", 1), Level("qwDo BfKJXI", 3)])

design=[atISnwmWtks,oO_XCRR,IyVpmnqGLUUB]
crossing=[atISnwmWtks,oO_XCRR,IyVpmnqGLUUB]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3_0"))

### END
