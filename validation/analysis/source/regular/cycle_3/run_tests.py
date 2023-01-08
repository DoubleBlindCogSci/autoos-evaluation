import os
from rouge_score import rouge_scorer
import pandas as pd

###
EXCLUDES = [(7,3,0),(8,3,0),(9,3,0),(6,3,1),(7,3,1),(8,3,1),(9,3,1),(9,2,1)]
NO_COMPILE = [(9,3,1),(5,3,0)]

