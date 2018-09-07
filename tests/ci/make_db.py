import os
import shutil
import yaml

import ixmp
import message_ix

from message_ix import macro

from paths import dbpath



def main():
    if os.path.exists(dbpath):
        shutil.rmtree(dbpath)

    mp = ixmp.Platform(dbpath, dbtype='HSQLDB')
    with open('scenarios.yaml', 'r') as f:
        for name, data in yaml.load(f).items():
            scen = message_ix.Scenario(
                mp, data['model'], data['scenario'], version='new')
            macro.init(scen)
            scen.read_excel(name + '.xlsx', add_units=True)
            scen.commit('saving')


if __name__ == '__main__':
    main()
