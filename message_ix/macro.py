init = {'macro':
        {'set': {'node': [],
                 'type_node': [],
                 'cat_node': ['type_node','node'],
                 'year': [],
                 'commodity': [],
                 'level': [],
                 'type_year': [],
                 'cat_year': ['type_year','year'],
                 'sector': [],
                 'mapping_macro_sector': ['sector', 'commodity', 'level'],
                 },
         'add_set': {'type_node': ['economy'],
                     'type_year': ['baseyear_macro','initializeyear_macro'],
                     'cat_year': ['baseyear_macro.2010','initializeyear_macro.2010']
                     },
         'par': {'demand_MESSAGE': ["node", "sector", "year"],
                 'price_MESSAGE': ["node", "sector", "year"],
                 'cost_MESSAGE': ["node","year"],
                 'gdp_calibrate': ["node","year"],
                 'historical_gdp': ["node","year"],
                 'MERtoPPP': ["node","year"],
                 'kgdp': ['node'],
                 'kpvs': ['node'],
                 'depr': ['node'],
                 'drate': ['node'],
                 'esub': ['node'],
                 'lotol': ['node'],
                 'p_ref': ["node","sector"],
                 'lakl': ['node'],
                 'prfconst': ["node","sector"],
                 'grow': ["node","year"],
                 'aeei': ["node", "sector", "year"],
                 },
         'var': {'DEMAND': ["node","commodity","level","year","time"],
                 'PRICE': ["node","commodity","level","year","time"],
                 'COST_NODAL': ["node", "year"],
                 'COST_NODAL_NET': ["node", "year"],
                 'GDP': ["node","year"],
                 'I': ["node","year"],
                 'C': ["node","year"],
                 'K': ["node","year"],
                 'KN': ["node","year"],
                 'Y': ["node","year"],
                 'YN': ["node","year"],
                 'EC': ["node","year"],
                 'UTILITY': [],
                 'PHYSENE': ["node","sector","year"],
                 'PRODENE': ["node","sector","year"],
                 'NEWENE': ["node","sector","year"],
                 'grow_calibrate': ["node","year"],
                 'aeei_calibrate': ["node","sector","year"],
                 },
        'equ': {'COST_ACCOUNTING_NODAL': ["node", "year"],
                }
         }}

def _init_macro(s):
    for i in init['macro']['set']:
        try:
            print('Initiating', i)
            s.init_set(i, idx_sets=init['macro']['set'][i])
        except:
            continue

    for i in init['macro']['add_set']:
        try:
            print('Initiating', i)
            s.add_set(i, init['macro']['add_set'][i])
        except:
            continue

    for i in init['macro']['par']:
        try:
            print('Initiating', i)
            s.init_par(i, idx_sets=init['macro']['par'][i])
        except:
            continue

    for i in init['macro']['var']:
        try:
            print('Initiating', i)
            s.init_var(i, idx_sets=init['macro']['var'][i])
        except:
            continue

    for i in init['macro']['equ']:
        try:
            print('Initiating', i)
            s.add_equ(i, idx_sets=init['macro']['equ'][i])
        except:
            continue


