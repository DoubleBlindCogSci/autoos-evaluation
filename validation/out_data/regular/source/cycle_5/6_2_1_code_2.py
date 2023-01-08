from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
T_hdyKWgNx_aq = Factor("T2hdyKWgNx#aq", ["ivFHOCJEx)qy#", "a07IdQAQRf", "DRdH nBIO", "<kl#?JvIE#G", "naOZmdGA", Level("%oxVxiI(", 1), "NmjVDdgzkkAh"])
FwK2y^l CGt;U = Factor("FwK2y^l CGt;U", [Level("DOxJnlZahqkFT", 2), "DzXgDP(lo", "ruD}CjaBOIqy", "!SqbozoR", Level("Y]nhb5joP", 2), "qBet1kqGlKW", "l4|IHhKDSk"])

design=[T_hdyKWgNx_aq]
crossing=[T_hdyKWgNx_aq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_1"))

### END
