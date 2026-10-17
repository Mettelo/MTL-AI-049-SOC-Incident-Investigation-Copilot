"""Frozen event reconstruction; no incident response actions are executed."""
import json
from datetime import datetime

def prepare(path,meeting):
    bundle=json.loads(path.read_text(encoding='utf-8'))
    techniques={}
    for obj in bundle['objects']:
        if obj['type']!='attack-pattern' or obj.get('revoked') or obj.get('x_mitre_deprecated'): continue
        for ref in obj.get('external_references',[]):
            if ref.get('source_name')=='mitre-attack':
                techniques[ref['external_id']]={'name':obj['name'],'description':obj.get('description',''),
                    'url':ref.get('url'),'stix_id':obj['id'],'modified':obj['modified']}
    return {'version':'Enterprise ATT&CK 17.1','techniques':techniques}

def build(data):
    evidence={}; records=[]; entities={}; seen=set()
    def add(kind,text,details,cites):
        records.append({'id':f'R{len(records)+1:04d}','kind':kind,'text':text,'details':details,'citations':cites})
    events=[]
    for e in data['events']:
        assert e['id'] not in seen, 'Duplicate event ID'
        seen.add(e['id'])
        dt=datetime.fromisoformat(e['timestamp'].replace('Z','+00:00'))
        assert dt.tzinfo, 'Timezone required'
        events.append((dt,e))
    for _,e in sorted(events,key=lambda p:(p[0],p[1]['id'])):
        text=json.dumps(e,sort_keys=True)
        evidence[e['id']]={'text':text,'locator':data['scenario']+'/'+e['id']}
        cite={'source':e['id'],'quote':text}
        add('observed_event',e['summary'],{'timestamp':e['timestamp'],'host':e['host'],'user':e.get('user')},[cite])
        for field in ('host','user','process_guid','src_ip','dst_ip'):
            if e.get(field): entities.setdefault((field,e[field]),[]).append(cite)
        # Exact event predicates, never a model-generated technique ID.
        mapping={'powershell_execution':'T1059.001','scheduled_task_created':'T1053.005','credential_dump_alert':'T1003'}
        tid=mapping.get(e['event_type'])
        if tid and tid in data['attack']['techniques']:
            t=data['attack']['techniques'][tid]; key='attack:'+tid
            evidence[key]={'text':t['name']+'\n'+t['description'],'locator':t['url'],'version':data['attack']['version']}
            add('attack_hypothesis',tid+' '+t['name'],{'confidence':'candidate','reason':'event_type predicate; analyst must verify behaviour',
                'stix_id':t['stix_id'],'recommendation':'Inspect original telemetry and authorised change records; seek independent corroboration.'},
                [cite,{'source':key,'quote':t['name']}])
    for (field,value),cites in sorted(entities.items()):
        if len(cites)>1:
            add('correlation',f'Shared {field}: {value}',{'relationship':'shared value; does not prove causation'},cites)
    if events:
        first=sorted(events,key=lambda p:p[0])[0][1]
        add('analyst_handover','Validate telemetry coverage, investigate correlated entities and document alternative explanations.',
            {'unknowns':['Initial access not established','Compromise and exfiltration not established'],
            'next_steps':['Check clock offsets and missing telemetry','Verify authorised administration','Preserve original event evidence'],
            'actions_executed':False},[{'source':first['id'],'quote':first['summary']}])
    return {'project':'MTL-AI-049','mode':'deterministic-reconstruction','evidence':evidence,'records':records,
        'scenario':data['scenario'],'attack_version':data['attack']['version']}
