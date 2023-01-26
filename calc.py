from quarkpy.functional import *

print("Hallo")

yc = BuildYC(Name="crv", Ccy="EUR", Instruments=[["1y", 5], ["5y", 10]])

acc = FixedLeg(yc, [["Template", "All"], ["QuarkId", "1"]], 1, 4, EndDate="2y")

help(acc)