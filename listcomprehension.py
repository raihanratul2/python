# আপনার কাছে কিছু দেশের নামের লিস্ট আছে: countries = ["Bangladesh", "India", "USA", "UK", "Canada", "UAE"]
# যে দেশগুলোর নাম ৫ অক্ষরের চেয়ে বড়, সেগুলোকে ছোট হাতের অক্ষরে (lowercase) রূপান্তর করুন।

countries = ["Bangladesh", "India", "USA", "UK", "Canada", "UAE"]

ct = list(map(lambda x : x.lower() if len(x)>5 else x.upper(), countries))
print(ct)


ct2 = [x.lower() if len(x)>5 else x.upper() for x in countries]

print(list(ct2))