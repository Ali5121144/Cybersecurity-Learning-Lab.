import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score == 5:
        return "Strong password ✅", feedback
    elif score >= 3:
        return "Medium password ⚠️", feedback
    else:
        return "Weak password ❌", feedback


password = input("Enter password to check: ")
result, feedback = check_password_strength(password)

print("\nResult:", result)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
