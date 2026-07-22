import csv
import os

FILENAME = "grades.csv"

def load_grades(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return None
    rows = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    if not rows:
        print(f"Error: {filename} is empty.")
        return None
    return rows

def main():
    rows = load_grades(FILENAME)
    if rows is None:
        return

    total_weight = 0
    summative_weight = 0
    formative_weight = 0
    summative_score = 0
    formative_score = 0
    failed_formatives = []

    for row in rows:
        try:
            weight = float(row["weight"])
            score = float(row["score"])
            category = row["category"].strip()
            name = row["assignment"].strip()
        except (ValueError, KeyError):
            print(f"Skipping malformed row: {row}")
            continue

        if not (0 <= score <= 100):
            print(f"Invalid score for {name}: {score} (must be 0-100)")
            return

        total_weight += weight

        if category == "Summative":
            summative_weight += weight
            summative_score += (score * weight / 100)
        elif category == "Formative":
            formative_weight += weight
            formative_score += (score * weight / 100)
            if score < 50:
                failed_formatives.append((name, weight))
        else:
            print(f"Unknown category for {name}: {category}")
            return

    if total_weight != 100:
        print(f"Weight validation failed: total weight is {total_weight}, expected 100.")
        return
    if summative_weight != 40:
        print(f"Weight validation failed: Summative weight is {summative_weight}, expected 40.")
        return
    if formative_weight != 60:
        print(f"Weight validation failed: Formative weight is {formative_weight}, expected 60.")
        return

    total_grade = summative_score + formative_score
    gpa = (total_grade / 100) * 5.0

    summative_pct = (summative_score / summative_weight) * 100
    formative_pct = (formative_score / formative_weight) * 100

    passed = summative_pct >= 50 and formative_pct >= 50
    status = "PASSED" if passed else "FAILED"

    print(f"Summative %: {summative_pct:.2f}")
    print(f"Formative %: {formative_pct:.2f}")
    print(f"Total Grade: {total_grade:.2f}")
    print(f"GPA: {gpa:.2f}")
    print(f"Status: {status}")

    if failed_formatives:
        max_weight = max(w for _, w in failed_formatives)
        eligible = [n for n, w in failed_formatives if w == max_weight]
        print(f"Resubmission eligible: {', '.join(eligible)}")
    else:
        print("No resubmission needed.")

main()
