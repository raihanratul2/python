import re

text = "234,23523.235324.2353223,234"

# ধাপ ১: সব ইংরেজি অক্ষর [a-zA-Z] খুঁজে তা খালি স্ট্রিং "" দিয়ে বদলে দেওয়া
# cleaned_text = re.sub(r"[a-zA-Z]+", "", text)

# ধাপ ২: কমা "," এবং পয়েন্ট "." গুলোকে নিউলাইন "\n" দিয়ে বদলে দেওয়া
final_output = re.sub(r"[,.]", "\n", text)

print(final_output)