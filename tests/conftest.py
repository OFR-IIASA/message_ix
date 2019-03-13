import os
import pytest
import shutil
import tempfile

import ixmp


here = os.path.dirname(os.path.realpath(__file__))


def tempdir():
    return os.path.join(tempfile._get_default_tempdir(),
                        next(tempfile._get_candidate_names()))


def create_local_testdb(db='ixmptest'):
    # copy testdb
    dst = tempdir()
    test_props = os.path.join(dst, 'test.properties')
    src = os.path.join(here, 'testdb')
    shutil.copytree(src, dst)

    # create properties file
    fname = os.path.join(here, 'testdb', 'test.properties_template')
    with open(fname, 'r') as f:
        lines = f.read().format(here=dst.replace("\\", "/"), db=db)
    with open(test_props, 'w') as f:
        f.write(lines)

    return test_props


def launch_mp(test_props):
    # start jvm, launch Platform and connect to testdb (reconnect if closed)
    ixmp.start_jvm()
    mp = ixmp.Platform(test_props)
    mp.open_db()
    return mp


@pytest.fixture(scope="session")
def test_mp():
    yield launch_mp(create_local_testdb())


@pytest.fixture(scope="session")
def test_legacy_mp():
    yield launch_mp(create_local_testdb('message_ix_legacy'))


@pytest.fixture(scope="session")
def test_mp_props():
    test_props = create_local_testdb()

    # start jvm
    ixmp.start_jvm()

    yield test_props
