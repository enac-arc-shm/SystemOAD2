from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/webhook/", methods=["POST", "GET"])
def webhook_whatsapp():
    if request.method == "GET":
        if request.args.get('hub.verify_token') == "HolaNovato":
            return request.args.get('hub.challenge')
        else:
          return "Error de autentificacion."
    data=request.get_json()
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
    f = open("comandos.txt", "w")
    f.write(str(data))
    f.close()
    return jsonify({"status": "success"}, 200)

#INICIAMSO FLASK
if __name__ == "__main__":
  app.run(debug=True)