from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tmxw = Factor("tmxw", ["mziisl","gyd","twfm","xnr","pxy"])
def is_adtfo_nndknu(tmxw):
    return tmxw != "twfm" and tmxw == "xnr"
def is_adtfo_gbatej(tmxw):
    return not is_adtfo_nndknu(tmxw)
adtfo= Factor("adtfo", [DerivedLevel("nndknu", WithinTrial(is_adtfo_nndknu, [tmxw])), DerivedLevel("gbatej", WithinTrial(is_adtfo_gbatej, [tmxw]))])

design=[tmxw,adtfo]
crossing=[adtfo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
