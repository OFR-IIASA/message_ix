
from message_ix import Scenario
from message_ix import macro

msg_args = ('canning problem (MESSAGE scheme)', 'standard')


def test_init(test_mp):
    scen = Scenario(test_mp, *msg_args)
    scen.check_out()
    macro.init(scen)
    scen.commit('foo')
    scen.solve()
