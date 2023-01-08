### REGULAR FACTORS
hcwl = Factor("hcwl", ["yuf", "mso"])
mdvxwl = Factor("mdvxwl", ["ywadjh", "fskl"])
sql = Factor("sql", ["yuf", "mso"])
mjwrx = Factor("mjwrx", ["ywadjh", "fskl"])
iaa = Factor("iaa", ["uqbw", "gwzp"])
### DERIVED FACTORS
##
def is_uid_nfp(sql, mdvxwl):
    return sql == mdvxwl
def is_uid_waj(sql, mdvxwl):
    return not is_uid_nfp(sql, mdvxwl)
uid= Factor("uid", [DerivedLevel("nfp", WithinTrial(is_uid_nfp, [sql, mdvxwl])), DerivedLevel("waj", WithinTrial(is_uid_waj, [sql, mdvxwl]))])
### EXPERIMENT
constraints = [ExactlyKInARow(2, (mjwrx, "waj"))]
crossing = [uid, hcwl]
design=[hcwl,mdvxwl,sql,mjwrx,iaa]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
