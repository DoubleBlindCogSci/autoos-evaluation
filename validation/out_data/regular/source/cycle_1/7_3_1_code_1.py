from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/7_3_1"))
### END