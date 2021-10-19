import pylog2pdf
from pylog2pdf import LoggedClass, LoggedFunction


@LoggedClass
class Sun:
    distance: float
    radius: float

    def some_calculation(self):
        pass

    def other_calculation(self):
        pass


class ThisThesis(Sun):
    distance = 1.5e8
    radius = 696e6


class OtherThesis(Sun):
    distance = 1.4959787e8
    radius = 695e6


@LoggedFunction
def sample_function1():
    pass


@LoggedFunction
def sample_function2():
    pass


def test_empty():
    for v in pylog2pdf.LOG.values():
        assert not v


def test_function():
    sample_function1()
    assert pylog2pdf.LOG["function"] == ["sample_function1"]


def test_multiple_functions():
    sample_function2()
    assert pylog2pdf.LOG["function"] == ["sample_function1", "sample_function2"]


def test_class():
    ThisThesis()
    assert pylog2pdf.LOG["Sun"] == "ThisThesis"


def test_overwritten():
    OtherThesis()
    assert pylog2pdf.LOG["Sun"] == "OtherThesis"


def test_manually_add():
    pylog2pdf.LOG["radius"] = OtherThesis.radius
    assert pylog2pdf.LOG["radius"] == OtherThesis.radius
