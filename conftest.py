import shutil
import os
import zipfile
import pytest


@pytest.fixture
def test_add_in_zip_file():
    os.chdir('resources')
    with zipfile.ZipFile('archive.zip', 'w') as zp:
        zp.write('file.txt')
        zp.write('file.xls')
        zp.write('file.xlsx')
        zp.write('file.pdf')

    if not os.path.isdir('../tmp'):
        os.mkdir('../tmp')
    shutil.move('archive.zip', os.path.join('../tmp', 'archive.zip'))
    yield
