import database as DB


#DB.add_one("Laura", "Smith", "laura@smith.com")
#DB.delete_one('6')

#many_customers = [
#        ('Brenda','Smitherton','brenda@smitherton.com'), 
#        ('Johsua','Raintree','joshua@raintree.com')
#        ]
#DB.add_many(many_customers)

DB.email_lookup("joshua@raintree.com")
print('-----------------------------------')
DB.show_all()

