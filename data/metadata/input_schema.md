# Input contract

Input: scenario, synthetic flag, events[], attack.version and attack.techniques. Event fields: unique id, ISO timestamp with timezone, host, event_type, summary; optional user, process_guid, src_ip, dst_ip. Unknown event types remain timeline evidence, not ATT&CK mappings. ATT&CK entries preserve name, description, URL, STIX ID and modified. Six fixtures are authored synthetic scenarios, never production logs. To refresh the ATT&CK snapshot, prepare the full bundle and explicitly replace the attack object in each selected input; version-lock it before evaluation.
