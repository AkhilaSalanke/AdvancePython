from reader import read_col
from FinalTest1 import Print_NumofCaptains
import pandas as pd

class TestClass:
    def test_TiedmatchCaptains(self):
        df = pd.read_csv("captains.txt")
        Exp = (df[df["Tied"]>0]["Player"].count())
        assert Print_NumofCaptains(read_col("captains.txt", "Tied", int)) == Exp

