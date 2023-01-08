from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_ulhEIFPmeJSJ = Factor("]ulhEIFPmeJSJ", [Level("Dwpo", 3), Level("7n0ydtuaiU_t(", 1), Level("AFBQ{KYt]fr", 1), Level("kXk|wYLB5u2", 2), Level("WuegvJYYn9qv", 1), Level("iRHYrymSM", 1), Level("8K1yRQ^RE", 1), Level("Tsr", 1), Level("GDe52DggggTKB", 1), Level("reOS]reif", 1)])
VJLkA_ = Factor("VJLkA}", [Level("WGJHzqlek", 1), Level("|DYDBrO^ffLh", 1), Level("yGe#erym", 1), Level("swix33", 1), Level("Blwe:sUNz^gsrr", 1), Level("vSDdLAZb", 1), Level("FYp{hvfY?qa", 4), Level("jQuH", 1), Level("@IxWFlz>D^jm9T", 1), Level("gvjD", 1)])
ghFYiRoNS = Factor("ghFYiRoNS", ["cMLo2i", "RrrRufq6syg3E", "}YPvGjLBhCC5gB", "VARXTTx", "8:V", "CrHT|KdTRDL", "Ajjj 8Jtl", "xRKUH>UdNjnpV", "hlZs", "5njxHRsA6k"])
_b_XDFe___m = Factor("[b6XDFe}}:m", [Level("_Uj", 3), Level("gXOxQuK", 1), Level("JqLBkFqmb1e", 1), Level("~bxvduQ|", 1), Level("y;JA", 1), Level("WjIwj%U", 1), Level("f@%WtkW", 1), Level("OtjyBLn&SWdC", 1), Level("ooxmiQdV5A", 1), Level("hyhIBh)rE", 1), Level("UhOzDdN", 1), Level("wdvQPk7i", 4), Level("Bxg", 1), Level("yCV@bfYbI", 1)])

design=[_ulhEIFPmeJSJ,VJLkA_,ghFYiRoNS,_b_XDFe___m]
crossing=[_ulhEIFPmeJSJ,VJLkA_,ghFYiRoNS,_b_XDFe___m]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/10_4_0"))

### END
