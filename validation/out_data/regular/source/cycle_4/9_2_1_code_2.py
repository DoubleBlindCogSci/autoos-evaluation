from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZkX_tIBFirTJ = Factor("ZkX}tIBFirTJ", [Level("NHeid", 3), "gxuEEmGPjd", "kg_YYOZ", "OQB", "WJACKaffc<G", "vt;", "E7QCPK", "MTM", "s>EN8htD", "R#U"])
ayQBYUg_ = Factor("ayQBYUg%", ["TDpwahS#TACXo", "XRkx5$JmVx", "mWUEB[oovwzi", "Q3F6I2a6tb5TF(", "jGa>L^3~r", "OY$", "1fq<E(6 &JxBG", "%a6UN)zmz_!a4", "fIIDMx^{iX46w["])

design=[ZkX_tIBFirTJ,ayQBYUg_]
crossing=[ZkX_tIBFirTJ,ayQBYUg_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_2_1"))

### END
