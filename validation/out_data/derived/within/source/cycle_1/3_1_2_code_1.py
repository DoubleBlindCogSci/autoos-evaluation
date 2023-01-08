from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ikgamn = Factor("ikgamn", ["ucsa","inj","udhmv","gaebof","npc","vhu","loyim"])
def wswdbp(ikgamn):
     return ikgamn == "udhmv"
def ntpfhj(ikgamn):
     return ikgamn == "gaebof"
def krabcl(ikgamn):
     return (ikgamn != "udhmv") and (ikgamn != "gaebof")
zqa = DerivedLevel("frpat", WithinTrial(wswdbp, [ikgamn]))
rsuo = DerivedLevel("otrfsn", WithinTrial(ntpfhj, [ikgamn]))
ymjl = DerivedLevel("pwai", WithinTrial(krabcl, [ikgamn]))
pwrfho = Factor("xvidu", [zqa, rsuo, ymjl])

### EXPERIMENT
design=[ikgamn,pwrfho]
crossing=[pwrfho]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END