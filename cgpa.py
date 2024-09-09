def calculate_cgpa(grades, credit_hours):
    total_points = sum(grade * credit for grade, credit in zip(grades, credit_hours))
    total_credits = sum(credit_hours)
    cgpa = total_points / total_credits
    return cgpa

# Example usage
grades = [8.5, 9.0, 7.5, 8.0]  # Your grades for each semester
credit_hours = [20, 22, 18, 20]  # Corresponding credit hours for each semester

cgpa = calculate_cgpa(grades, credit_hours)
print(f"Your CGPA is: {cgpa:.2f}")
