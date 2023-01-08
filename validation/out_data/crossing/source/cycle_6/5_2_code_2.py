from sweetpea import *
import os
_dir=os.path.dirname(__file__)
pjmy = Factor("pjmy", ["xvrb", "tjmz"])
lusfem = Factor("lusfem", ["oxvc", "omcx"])
zsta = Factor("zsta", ["lbnkco", "rpk"])
vae = Factor("vae", ["xkpucs", "vxrft"])
dpx = Factor("dpx", ["aina", "izvh"])
rwf = Factor("rwf", ["ktjd", "zhfxox"])
eyik = Factor("eyik", ["lutgng", "oguc"])
tqkcmk = Factor("tqkcmk", ["diwa", "fhnprz"])
uog = Factor("uog", ["ipssyq", "ayzcg"])
deayhu = Factor("deayhu", ["lyrfma", "iagvfk"])
zpa = Factor("zpa", ["qgxok", "dlkmzh"])
ame = Factor("ame", ["flhz", "snx"])
jrbu = Factor("jrbu", ["mkecrz", "tpqsvu"])
dzwu = Factor("dzwu", ["txb", "vsm"])
ymwjh = Factor("ymwjh", ["fubc", "xqljtv"])
constraints = []
crossing = [[pjmy, lusfem, zsta], [vae, dpx, rwf], [eyik, tqkcmk, uog], [deayhu, zpa, ame], [jrbu, dzwu, ymwjh]]


design=[pjmy,lusfem,zsta,vae,dpx,rwf,eyik,tqkcmk,uog,deayhu,zpa,ame,jrbu,dzwu,ymwjh]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2"))

### END