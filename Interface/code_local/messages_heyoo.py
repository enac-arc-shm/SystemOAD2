from heyoo import WhatsApp

class WhatsappService:

    def __init__(self, cellphone, server):
        self.cellphone = cellphone
        self.server = server


    def __str__(self) -> str:
        pass


    @property
    def cellphone (self):
        return self._cellphone
    
    
    @cellphone.setter
    def cellphone (self, cellphone):
        if not cellphone:
            raise ValueError("Missing value for cellphone")
        self._cellphone = cellphone


    @property
    def server (self):
        return self._server
    

    @server.setter
    def server (self, server):
        if not server:
            raise ValueError("Missing value for server")
        self._server = server    


    @classmethod
    def objectMessageWa(self):
        token = 'EAACrEJCbRiIBAGSl6CdaZBgJUARr9oOm9iAScRKbxc35CZCRZAj6ud2KmLApJDBn2hqddHVOU8ndUZC3dUFWuWSfpxYUhQfU1uxxUhYZCxLOMTFgPaVJCgbIR8fTCgtWLnUXCPx1tFN8oFzcmFFp0dZAZAv0C2AWo2UZB1i2X8uyKbxjDEwNxbWeaDHGMziCt6jvZBi2ZAMADPH2tny6wz2gtb'
        idNumCellphone = '107311828972865'
        return WhatsApp(token,idNumCellphone)
    

    def sendMessage(self, message):
        messageWa = self.objectMessageWa()
        messageWa.send_message(message, self.cellphone)


    def sendButtonService(self, service, status):
        messageWa = self.objectMessageWa()
        messageWa.send_button(
        recipient_id=self.cellphone,
        button={
            "header": f"Issues service {service} on {self.server}",
            "body": f"Currently the service *{service}* of the {self.server} server is {status}, select a countermeasure action.",
            "footer": "Remember that any action has a direct impact",
            "action": {
                "button": "Prevention actions",
                "sections": [
                    {
                        "title": f"{self.server} - {service}",
                        "rows": [
                            {
                                "id": "row 1", 
                                "title": f"systemctl start {service}",
                                "description": "Try to lift service"},
                            {
                                "id": "row 2",
                                "title": f"systemctl restart {service}",
                                "description": "Reload the service",                                
                            },
                            {
                                "id": "row 3",
                                "title": f"systemctl stop {service}",
                                "description": "Stop service",
                            },
                            {
                                "id": "row 4",
                                "title": f"systemctl status {service}",
                                "description": "Check status and parameter",
                            },
                        ],
                    }
                ],
            },
        },
    )
    

    def sendReplyButtonServer(self):
        messageWa = self.objectMessageWa()
        messageWa.send_reply_button(
            recipient_id=self.cellphone,
            button={
                "type": "button",
                "body": {
                    "text": "Carefull, any action must be autenticate first  "
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "b1",
                                "title": f"Shutdown -h now {self.server}"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "b2",
                                "title": f"Restart -h now {self.server}"
                            }
                        }
                    ]
                }
            },
        )
