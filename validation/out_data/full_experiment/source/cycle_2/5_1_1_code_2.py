from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
hcwl = Factor("hcwl", ["yuf", "mso"])
mdvxwl = Factor("mdvxwl", ["ywadjh", "fskl"])
sql = Factor("sql", ["yuf", "mso"])
mjwrx = Factor("mjwrx", ["ywadjh", "fskl"])
iaa = Factor("iaa", ["uqbw", "gwzp"])
def is_uid_nfp(sql, mdvxwl):
    return sql == mdvxwl
def is_uid_waj(sql, mdvxwl):
    return not is_uid_nfp(sql, mdvxwl)
uid= Factor("uid", [DerivedLevel("nfp", WithinTrial(is_uid_nfp, [sql, mdvxwl])), DerivedLevel("waj", WithinTrial(is_uid_waj, [sql, mdvxwl]))])
constraints = [ExactlyKInARow(2, mjwrx)]
crossing = [uid, hcwl]

design=[hcwl,mdvxwl,sql,mjwrx,iaa,uid]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_1"))
