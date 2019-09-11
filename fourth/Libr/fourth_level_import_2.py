from fourth.Libr import one
aa = "sss" + one.a

from . import one
import fourth.Libr.one

from fourth.Libr import *
print(one.a)

from ..Model import one
aa = "ss" + one.a

