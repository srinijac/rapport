from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa3ee54b5030f3a2b427107e4ff8517af"
# Your Auth Token from twilio.com/console
auth_token  = "5f5479d1ea747a53454b61d812376cc4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15105986092",
    from_="+12052930681",
    body="wassup bro how's ur shit")

print(message.sid)
