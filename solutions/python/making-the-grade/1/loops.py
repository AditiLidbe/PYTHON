def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students (score <= 40)."""
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """Return scores at or above the given threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create grade thresholds for D, C, B, A based on highest score."""
    # Failing is <= 40
    # Remaining range is divided into 4 equal intervals
    interval = (highest - 40) // 4

    return [
        41,
        41 + interval,
        41 + interval * 2,
        41 + interval * 3
    ]


def student_ranking(student_scores, student_names):
    """Return ranking strings in descending order."""
    result = []
    for index in range(len(student_scores)):
        rank = index + 1
        result.append(f"{rank}. {student_names[index]}: {student_scores[index]}")
    return result


def perfect_score(student_info):
    """Return first student with perfect score of 100."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []