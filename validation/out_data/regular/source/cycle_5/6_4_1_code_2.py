from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yoaFxqvtb = Factor("yoaFxqvtb", ["k8NeS", "xYTLCkuFMA(x", Level("WaPjr", 1), "5ELMv^ujl^XfnQ", "mast_Q", "xpAigKIpHcu"])
_ctPvTkxcwR__Y = Factor("4ctPvTkxcwR@}Y", ["L ggETb$r", "XoX", "iT07x", Level("n?hZi", 3), Level("qfDj", 1), "<jilf"])
nvfwNpK_OB = Factor("nvfwNpK_OB", ["ZhHc|Oj%PhJxBW", "jr!MvOg", "cYGIHs", "m?X~BKgzYe", "AdzrNrKDD?5", "5W4SA"])
OA_aBte_c = Factor("OA[aBte4c", ["hLpIlIUs!ICYP", Level("aBrUguFn", 3), "{iub", ";PFkI#n2", "YjP[CZyBpV4sX", "|f?", "r&sZ"])

design=[yoaFxqvtb,_ctPvTkxcwR__Y,nvfwNpK_OB,OA_aBte_c]
crossing=[yoaFxqvtb,_ctPvTkxcwR__Y,nvfwNpK_OB,OA_aBte_c]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_4_1"))

### END
