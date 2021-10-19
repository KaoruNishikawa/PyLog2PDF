from pathlib import Path
import pytest
import shutil

import pylog2pdf

PDF_PATH = Path("tests/sample.pdf")


@pytest.fixture(scope="module")
def SAMPLE_PATH(tmp_path_factory):
    copy_to = tmp_path_factory.mktemp("data") / "sample.pdf"
    shutil.copy(str(PDF_PATH), str(copy_to))
    return copy_to


@pytest.mark.usefixtures("SAMPLE_PATH")
def test_empty(SAMPLE_PATH):
    save_path = pylog2pdf.write_log(SAMPLE_PATH, {})
    assert save_path == SAMPLE_PATH

    log = pylog2pdf.read_log(SAMPLE_PATH)
    assert log == {}


@pytest.mark.usefixtures("SAMPLE_PATH")
def test_save(SAMPLE_PATH):
    pylog2pdf.LOG["test"] = "test string"
    save_path = pylog2pdf.write_log(SAMPLE_PATH)
    assert save_path == SAMPLE_PATH

    log = pylog2pdf.read_log(SAMPLE_PATH)
    assert log["test"] == pylog2pdf.LOG["test"]


@pytest.mark.usefixtures("SAMPLE_PATH")
def test_manually(SAMPLE_PATH):
    save_path = pylog2pdf.write_log(SAMPLE_PATH, {"manually": "added"})
    assert save_path == SAMPLE_PATH

    log = pylog2pdf.read_log(SAMPLE_PATH)
    assert log["manually"] == "added"


@pytest.mark.usefixtures("SAMPLE_PATH")
def test_dict_in_dict(SAMPLE_PATH):
    save_path = pylog2pdf.write_log(SAMPLE_PATH, {"dict_": {"in_": "dict_"}})
    assert save_path == SAMPLE_PATH

    log = pylog2pdf.read_log(SAMPLE_PATH)
    assert log["dict_"] == {"in_": "dict_"}
