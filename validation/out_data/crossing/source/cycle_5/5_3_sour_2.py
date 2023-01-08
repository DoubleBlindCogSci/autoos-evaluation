from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
iwr = Factor("iwr", ["sswxtv", "jkuber"])
tpwu = Factor("tpwu", ["lfhpt", "yyvsxh"])
rxng = Factor("rxng", ["mfa", "pcpeov"])
xzm = Factor("xzm", ["hzjf", "dypphl"])
dkzxv = Factor("dkzxv", ["hci", "jjwp"])
rhjn = Factor("rhjn", ["klyu", "vzdql"])
gsy = Factor("gsy", ["odt", "lgnoh"])
sqzd = Factor("sqzd", ["tnb", "qmkjbq"])
nhagce = Factor("nhagce", ["jszi", "ywl"])
rkawni = Factor("rkawni", ["tmnohm", "bgemlq"])
xilc = Factor("xilc", ["nnifgz", "lhq"])
ixcig = Factor("ixcig", ["nip", "cgxdw"])
vfn = Factor("vfn", ["yrxq", "rpkn"])
zbzahn = Factor("zbzahn", ["brcgu", "ofpi"])
constraints = []
crossing = [[iwr, tpwu, rxng, xzm], [dkzxv, rhjn, gsy, sqzd], [nhagce, rkawni], [xilc, ixcig, vfn, zbzahn]]


design=[iwr,tpwu,rxng,xzm,dkzxv,rhjn,gsy,sqzd,nhagce,rkawni,xilc,ixcig,vfn,zbzahn]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/5_3_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/5_3_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [iwr, tpwu, rxng, xzm]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ dkzxv, rhjn, gsy, sqzd]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ nhagce, rkawni]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ xilc, ixcig, vfn, zbzahn]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
