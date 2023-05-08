from courserecommend import *
from electives import *

def test_showElectives():
    assert showElectives() == [cs503, cs513, cs516, cs521, cs522, cs524, cs526, cs541, cs545, cs546, cs548, cs549, cs554, cs555, cs558, cs559, cs562, cs573, cs574, cs576, cs578, cs583, cs584, cs600, cs615]