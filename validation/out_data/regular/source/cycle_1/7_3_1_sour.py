from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
u2fobII8o="Zkx"
vuT91V=[u2fobII8o,'dKWtWQrOAQFfz',"%>QH:WjhvIM","S$ OwGDsUW",Level("BPNO[Gkigk",8),"0viLZCm<qsj",'QxDuSEy',"E|YHXMn8ONxhIR"]
wym_pOC0TgZ=Factor("sZxB)k(",vuT91V)
Il4VgxK=Factor('hrYqFG',['ZrF',Level("r*a3yhl^t",6),"&HdXvp]dcIM",'lQTwqZ',Level('lJA5tcEWomCqB',10),"kzZKEWr^v","lJrxL(BNChimdM"])
A7JZuSF=["Qzq",'MCjEVcQ!~z~5V',Level('sNWxfAx(L]Sv',9),'yCYNI','%se2nV','IPeluGRK4I',"rex@G|y8{vpxPD"]
uuyqik_e=Factor('CTb',A7JZuSF)

### EXPERIMENT
design=[wym_pOC0TgZ,Il4VgxK,uuyqik_e]
crossing=[wym_pOC0TgZ,Il4VgxK,uuyqik_e]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/7_3_1_0.csv"))
nr_factors=3
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/7_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)