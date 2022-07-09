import pkg.mod1, pkg.mod2
from pkg.mod444 import *

pkg.mod1.foo()
pkg.mod2.bar()

print(dir())