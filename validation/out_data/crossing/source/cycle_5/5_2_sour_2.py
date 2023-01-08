from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
_dir=os.path.dirname(__file__)
gzjyk = Factor("gzjyk", ["ffbyf", "gcmey"])
suk = Factor("suk", ["jvg", "nvjcva"])
ugvn = Factor("ugvn", ["vasvin", "mnk"])
rulygd = Factor("rulygd", ["jse", "dpdmvc"])
phmylo = Factor("phmylo", ["lreyc", "fhh"])
vmn = Factor("vmn", ["vbm", "dmn"])
sbj = Factor("sbj", ["ktf", "wgt"])
wiqfxt = Factor("wiqfxt", ["tgtx", "uoh"])
nkaqzs = Factor("nkaqzs", ["mpewce", "flbzy"])
jcver = Factor("jcver", ["wwyar", "ccaie"])
zxbc = Factor("zxbc", ["wbaf", "hbwsly"])
fdk = Factor("fdk", ["wjh", "mxho"])
fnaowb = Factor("fnaowb", ["xhcom", "vwu"])
uqetk = Factor("uqetk", ["xdjls", "rfusu"])
taj = Factor("taj", ["jar", "xqw"])
htr = Factor("htr", ["uxgz", "elcb"])
xzwt = Factor("xzwt", ["kddbp", "ibp"])
constraints = []
crossing = [[gzjyk, suk, ugvn, rulygd], [phmylo, vmn, sbj, wiqfxt], [nkaqzs], [jcver, zxbc, fdk, fnaowb], [uqetk, taj, htr, xzwt]]


design=[gzjyk,suk,ugvn,rulygd,phmylo,vmn,sbj,wiqfxt,nkaqzs,jcver,zxbc,fdk,fnaowb,uqetk,taj,htr,xzwt]
sequence_code_1=trials_from_csv(os.path.join(_dir,'out_code_1/5_2_0.csv'))
sequence_code_2=trials_from_csv(os.path.join(_dir,'out_code_2/5_2_0.csv'))
p_code_1 = 0
p_code_2 = 0
crossing = [gzjyk, suk, ugvn, rulygd]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ phmylo, vmn, sbj, wiqfxt]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ nkaqzs]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ jcver, zxbc, fdk, fnaowb]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
crossing = [ uqetk, taj, htr, xzwt]
block = Block(design, crossing, [])
p_code_1 += block.test(sequence_code_1)["pValue"] >= 1
p_code_2 += block.test(sequence_code_2)["pValue"] >= 1
df = pd.read_csv(os.path.join(_dir, "result_sour_2.csv"))
df.loc[len(df.index)] = [p_code_1, p_code_2]
df.to_csv(os.path.join(_dir, "result_sour_2.csv"), index=False)
