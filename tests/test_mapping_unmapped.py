from ngr.mapping.unmapped import collect_unmapped
from ngr.models import Feature, LineageSegment

F = Feature('waveform', '波形', [LineageSegment('6G','Rel-20','full',['RAN1:10.2','RAN1:10.2.*'],None,{'RAN1':(124,None)})])
def parsed(items): return {'wg':'RAN1','meeting':126,'events':[{'agenda_item':i,'agenda_title':t,'heading_path':['6GR',t]} for i,t in items]}
def test_collects_only_unmapped_6g_and_rolls_children():
    assert collect_unmapped([F],[parsed([('10.8','ISAC')])],sixg_roots=['10']) == ['RAN1:10.8 ISAC']
    assert collect_unmapped([F],[parsed([('10.2','Waveform'),('9.1','AI')])],sixg_roots=['10']) == []
    assert collect_unmapped([F],[parsed([('10.8.1','a'),('10.8.2','b')])],sixg_roots=['10']) == ['RAN1:10.8 (2 个子项未归类)']


def test_uses_meeting_scoped_root_derived_from_6g_lineage():
    ran2 = Feature('rrc', 'RRC', [LineageSegment(
        '6G', 'Rel-20', 'full', ['RAN2:9.3.2'], None, {'RAN2': (133, None)})])
    meeting = {'wg': 'RAN2', 'meeting': 134, 'events': [
        {'agenda_item': '9.5', 'agenda_title': 'ISAC', 'heading_path': ['6GR', 'ISAC']},
        {'agenda_item': '10.1', 'agenda_title': 'Legacy session', 'heading_path': []},
    ]}
    assert collect_unmapped([ran2], [meeting]) == ['RAN2:9.5 ISAC']


def test_scoped_roots_do_not_treat_regular_meeting_as_special_session():
    ran2 = Feature('rrc', 'RRC', [LineageSegment(
        '6G', 'Rel-20', 'full', ['RAN2:9.3.2'], None, {'RAN2': (133, None)},
        meeting_start_suffixes=('bis',))])
    regular = {'wg': 'RAN2', 'meeting': 133, 'meeting_suffix': '', 'events': [
        {'agenda_item': '9.3.2', 'agenda_title': 'NR RRM prediction', 'heading_path': []},
    ]}
    special = {**regular, 'meeting_suffix': 'bis'}
    assert collect_unmapped([ran2], [regular]) == []
    assert collect_unmapped([ran2], [special]) == []
