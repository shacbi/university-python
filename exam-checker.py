# Student Examination Result Checker

print("=== UNIVERSITY RESULT CHECKER ===")

marks = float(input("gali your exam marks (0 - 100): "))

if marks >= 50:
    result = "PASSED"
    message = "hanbalyo! You passed the exam."
else:
    result = "FAILED"
    message = "waan ka xuma hay, you need to retake the exam."

print(f"\nFinal Result: {result}")
print(f"Message: {message}")