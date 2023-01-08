import os
from rouge_score import rouge_scorer
import pandas as pd

EXCLUDES = [(2, 1, 4), (3, 2, 4)]

NO_COMPILE = []
