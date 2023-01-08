from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dgnaub = Factor("dgnaub", ["kklua", "xpmns"])
tfaro = Factor("tfaro", ["jxcj", "jfwo"])
manzxm = Factor("manzxm", ["fzc", "xsfb"])
ped = Factor("ped", ["ksrxsh", "xirv"])
jlj = Factor("jlj", ["lnvgdl", "xnuoq"])
fonstm = Factor("fonstm", ["rmhl", "tehvak"])
liebp = Factor("liebp", ["nufeno", "bktzf"])
xhzlgr = Factor("xhzlgr", ["tifz", "fnejf"])
zvlsr = Factor("zvlsr", ["cik", "umo"])
bfgx = Factor("bfgx", ["xchb", "ijxg"])
petb = Factor("petb", ["aejq", "wtljsw"])
doucj = Factor("doucj", ["xuco", "yyxa"])
xaz = Factor("xaz", ["lnanh", "hcltqz"])
fesx = Factor("fesx", ["rcfo", "mprq"])

### EXPERIMENT
design=[dgnaub,tfaro,manzxm,ped,jlj,fonstm,liebp,xhzlgr,zvlsr,bfgx,petb,doucj,xaz,fesx]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_4_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_4_0.csv"))
nr_crossings=4
nr_factors=14
p_code_1 = 0
p_code_2 = 0
crossing = [dgnaub,tfaro,manzxm]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ped,jlj,fonstm]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [liebp,xhzlgr,zvlsr,bfgx]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [petb,doucj,xaz,fesx]
block = Block(design,crossing,[])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2, nr_crossings, nr_factors]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
