import tor
import time

API_KEY = "YOUR API KEY"
PROJECT_DOMAIN = "YOUR PROJECT DOMAIN"

api = tor.TorApi(API_KEY, PROJECT_DOMAIN)

ticket = {}
ticket["email"] = "your@email.address"
ticket["from_name"] = 'John Doe'
ticket["subject"] = 'lorem ipsum...'
ticket["body"] = 'lorem ipsum...'
ticket["html"] = False
ticket["date"] = time.time()
ticket["labels"] = ['label 1', 'label 2']
# poster lib required (http://pypi.python.org/pypi/poster/)
ticket["attachment"] = "attachment.txt"

ticket_result = api.new_ticket(ticket)
print "ticket %s, id %s" % (ticket_result["ticket"], ticket_result["id"])
