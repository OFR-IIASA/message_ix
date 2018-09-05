import yaml

import ixmp
import message_ix
from message_ix.macro import _init_macro


def main():
    mp = ixmp.Platform('scenario_db', dbtype='HSQLDB')
    with open('scenarios.yaml', 'r') as f:
        for name, data in yaml.load(f).items():
            scen = message_ix.Scenario(
                mp, data['model'], data['scenario'], version='new')
            _init_macro(scen)
            scen.read_excel(name + '.xlsx')
            scen.commit('saving')


if __name__ == '__main__':
    main()
