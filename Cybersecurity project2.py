import re

def check_password(password):
    score = 0

    if len(password) >= 8: score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1

    if score == 5:
        print("✅ Strong password!")
    elif score >= 3:
        print("⚠️ Medium password.")
    else:
        print("❌ Weak password.")

if __name__ == "__main__":
    pwd = input("Enter password: ")
    check_password(pwd)
