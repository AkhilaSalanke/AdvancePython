from reader import read_col
from FinalTest2 import Print_captainNames
import pandas as pd

class TestClass:
    def test_TiedcaptainNames(self):
        df = pd.read_csv("captains.txt")
        Exp = list((df[df["Tied"]>0]["Player"]))
        assert Print_captainNames() == Exp


