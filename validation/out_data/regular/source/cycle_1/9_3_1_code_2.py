from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aCxZeoeIL_juMW= Factor("aCxZeoeIL3juMW", [Level("u?v_KojSN|WPkS", 4), Level("Lq?FQcPOtb0nWj", 4), Level("v)StcoGOF", 3), "AxszFnNWuiI", "eweZMTbkNOD^", "dFcgB", "gHPSg", "QWNm", "gqeq"])
Yvxqae= Factor("Yvxqae", [Level(":@C tggT>F0)NH", 7), Level("NLsPUZqahHqnL", 1), Level("vZom[QL", 2), Level("ZMyqTbglCTDi0", 2), "NkTvHpRSBqz", "Btt7", "tkT$FZJ", "JLX)", "Bdm"])
mEpmn_lMKd_= Factor("mEpmn;lMKd?", [Level("TxWoCsPHzHTAV", 3), Level("RYY!oBjzT[qy", 5), "b6lkWxOWN", "|ZPSx1L", "0jeea", "9ZiOey7", "q WNxi:F[BY", "L6qqLLzMeAuz", "SoZ", "IfWH!xcHsJK"])

design=[aCxZeoeIL_juMW,Yvxqae,mEpmn_lMKd_]
crossing=[aCxZeoeIL_juMW,Yvxqae,mEpmn_lMKd_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/9_3_1"))

### END
