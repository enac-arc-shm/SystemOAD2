data={'object': 'whatsapp_business_account', 'entry': [{'id': '115068651521216', 'changes': [{'value': {'messaging_product': 'whatsapp', 'metadata': {'display_phone_number': '15550859481', 'phone_number_id': '107311828972865'}, 'contacts': [{'profile': {'name': 'UTTT'}, 'wa_id': '5217731922477'}], 'messages': [{'from': '5217731922477', 'id': 'wamid.HBgNNTIxNzczMTkyMjQ3NxUCABIYIEFFQ0IzNDZBMDczM0U2MkJCMENDMEM4QjUzQjQyQTYxAA==', 'timestamp': '1679810681', 'text': {'body': 'Hola mundo'}, 'type': 'text'}]}, 'field': 'messages'}]}]}

type = data['entry'][0]['changes'][0]['value']['messages'][0]['type']
if type == 'interactive':
    type = data['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['type'] 
    if type == 'button_reply':
        telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['button_reply']['title']
        idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
        timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
    else:
        telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
        mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['list_reply']['title']
        idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
        timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
else:
    telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
    timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
