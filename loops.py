usernames= ("Ratul","rafat","admin","rohim","korim","kuddus")
email = ("Ratul@email.com","rafat@email.com","admin@email.com","rohim@email.com","korim@email.com","kuddus@email.com")
user=[]
for username,email in zip(usernames,email):
    user.append({"username":username,"email":email})

print(user)