from ngr.mapping.unmapped import collect_unmapped
from ngr.models import Feature, LineageSegment

F = Feature('waveform', '波形', [LineageSegment('6G','Rel-20','full',['RAN1:10.2','RAN1:10.2.*'],None,{'RAN1':(124,None)})])
def parsed(items): return {'wg':'RAN1','meeting':126,'events':[{'agenda_item':i,'agenda_title':t,'heading_path':['6GR',t]} for i,t in items]}
def test_collects_only_unmapped_6g_and_rolls_children():
    assert collect_unmapped([F],[parsed([('10.8','ISAC')])],sixg_roots=['10']) == ['RAN1:10.8 ISAC']
    assert collect_unmapped([F],[parsed([('10.2','Waveform'),('9.1','AI')])],sixg_roots=['10']) == []
    assert collect_unmapped([F],[parsed([('10.8.1','a'),('10.8.2','b')])],sixg_roots=['10']) == ['RAN1:10.8 (2 个子项未归类)']
