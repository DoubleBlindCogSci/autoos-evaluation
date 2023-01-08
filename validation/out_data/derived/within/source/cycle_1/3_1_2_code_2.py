from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ikgamn= Factor("ikgamn", ["ucsa","inj","udhmv","gaebof","npc","vhu","loyim"])
def is_xvidu_frpat(ikgamn):
    return ikgamn == "udhmv"
def is_xvidu_otrfsn(ikgamn):
    return ikgamn == "gaebof"
def is_xvidu_pwai(ikgamn):
    return not (is_xvidu_frpat(ikgamn) or is_xvidu_otrfsn(ikgamn))
xvidu= Factor("xvidu", [DerivedLevel("frpat", WithinTrial(is_xvidu_frpat, [ikgamn])), DerivedLevel("otrfsn", WithinTrial(is_xvidu_otrfsn, [ikgamn])), DerivedLevel("pwai", WithinTrial(is_xvidu_pwai, [ikgamn]))])

design=[ikgamn,xvidu]
crossing=[xvidu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
