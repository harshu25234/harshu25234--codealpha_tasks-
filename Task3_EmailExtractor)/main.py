import re

# 🔹 Step 1: Input file se data read karo
with open("input.txt", "r") as file:
    data = file.read()

# 🔹 Step 2: Regex se email addresses nikaalo
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', data)

# 🔹 Step 3: Duplicate hatao aur sort karo
unique_emails = sorted(set(emails))

# 🔹 Step 4: Cleaned emails ko nayi file me save karo
with open("cleaned_emails.txt", "w") as file:
    for email in unique_emails:
        file.write(email + "\n")

# 🔹 Step 5: Terminal pe result print karo
print(f"{len(unique_emails)} unique emails extracted and saved to cleaned_emails.txt ✅")
