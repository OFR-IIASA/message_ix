import yaml

import ixmp
import message_ix


def main():
    mp = ixmp.Platform('scenario_db', dbtype='HSQLDB')
    with open('scenarios.yaml', 'r') as f:
        for name, data in yaml.load(f).items():
            scen = message_ix.Scenario(
                mp, data['model'], data['scenario'])
            scen.solve(model='MESSAGE-MACRO')

if __name__ == '__main__':
    main()
