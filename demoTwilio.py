from twilio.rest import Client 
 
account_sid = 'AC82da6297641708ee95f5fc5d02e9b90f' 
auth_token = '81a7609a1430638612c446aa0b6aeeef' 
client = Client(account_sid, auth_token) 

l = ['7683928306','9078101920']

for ph in l:
 
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='test message',      
                                to='whatsapp:+91{}'.format(ph)
                            ) 
 
print(message.sid)