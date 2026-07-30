from flask import Flask, render_template, request

app = Flask(__name__)


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():

    # -----------------------------
    # Student Details
    # -----------------------------
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    institution = request.form.get('institution')
    education_level = request.form.get('education_level')
    score_value = request.form.get('score')

    # -----------------------------
    # Subjects (checkbox values)
    # -----------------------------
    subjects = request.form.getlist('subjects')

    # -----------------------------
    # Other Inputs
    # -----------------------------
    skills = request.form.get('skills', '').lower()
    interest = request.form.get('interest', '').lower()
    work_style = request.form.get('work_style', '').lower()
    career_goal = request.form.get('career_goal', '').lower()
    hobbies = request.form.get('hobbies', '').lower()

    # -----------------------------
    # Career Scores
    # -----------------------------
    scores = {
        'Full Stack Developer': 0,
        'Software Engineer': 0,
        'AI / ML Engineer': 0,
        'Data Scientist': 0,
        'Cybersecurity Analyst': 0,
        'UI/UX Designer': 0,
        'Doctor': 0,
        'Business Analyst': 0,
        'Chartered Accountant': 0,
        'Teacher / Professor': 0
    }

    # -----------------------------
    # Subject Based Scoring
    # -----------------------------
    if 'Mathematics' in subjects:
        scores['Software Engineer'] += 15
        scores['AI / ML Engineer'] += 15
        scores['Data Scientist'] += 15
        scores['Chartered Accountant'] += 10

    if 'Computer Science' in subjects:
        scores['Full Stack Developer'] += 20
        scores['Software Engineer'] += 20
        scores['AI / ML Engineer'] += 15
        scores['Cybersecurity Analyst'] += 15

    if 'Science' in subjects:
        scores['Doctor'] += 15
        scores['AI / ML Engineer'] += 10

    if 'Biology' in subjects:
        scores['Doctor'] += 25

    if 'Business Studies' in subjects or 'Economics' in subjects:
        scores['Business Analyst'] += 20
        scores['Chartered Accountant'] += 20

    if 'English' in subjects:
        scores['Teacher / Professor'] += 10

    if 'Art' in subjects:
        scores['UI/UX Designer'] += 25

    # -----------------------------
    # Skills Based Scoring
    # -----------------------------
    if 'html' in skills or 'css' in skills or 'javascript' in skills:
        scores['Full Stack Developer'] += 25

    if 'java' in skills:
        scores['Software Engineer'] += 25

    if 'python' in skills:
        scores['AI / ML Engineer'] += 25
        scores['Data Scientist'] += 25

    if 'security' in skills or 'network' in skills:
        scores['Cybersecurity Analyst'] += 25

    if 'design' in skills or 'figma' in skills or 'drawing' in skills:
        scores['UI/UX Designer'] += 25

    if 'communication' in skills or 'teaching' in skills:
        scores['Teacher / Professor'] += 20

    if 'leadership' in skills or 'management' in skills:
        scores['Business Analyst'] += 20

    # -----------------------------
    # Interest Based Scoring
    # -----------------------------
    if 'technology' in interest or 'software' in interest:
        scores['Full Stack Developer'] += 20
        scores['Software Engineer'] += 20

    if 'ai' in interest:
        scores['AI / ML Engineer'] += 25
        scores['Data Scientist'] += 20

    if 'medical' in interest:
        scores['Doctor'] += 30

    if 'business' in interest:
        scores['Business Analyst'] += 25
        scores['Chartered Accountant'] += 25

    if 'design' in interest:
        scores['UI/UX Designer'] += 30

    if 'teaching' in interest:
        scores['Teacher / Professor'] += 25

    if 'government' in interest:
        scores['Teacher / Professor'] += 10

    # -----------------------------
    # Work Style Based Scoring
    # -----------------------------
    if 'problem solving' in work_style:
        scores['Software Engineer'] += 10
        scores['Data Scientist'] += 10

    if 'creative' in work_style:
        scores['UI/UX Designer'] += 10

    if 'helping people' in work_style:
        scores['Doctor'] += 10
        scores['Teacher / Professor'] += 10

    if 'leading teams' in work_style:
        scores['Business Analyst'] += 10

    if 'research' in work_style:
        scores['AI / ML Engineer'] += 10
        scores['Data Scientist'] += 10

    # -----------------------------
    # Career Goal Bonus
    # -----------------------------
    for career in scores.keys():
        if career.lower() in career_goal:
            scores[career] += 30

    # -----------------------------
    # Find Best Careers
    # -----------------------------
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    best_career, best_score = sorted_scores[0]
    second_career, second_score = sorted_scores[1]
    third_career, third_score = sorted_scores[2]

    # Limit score to 100
    best_score = min(best_score, 100)
    second_score = min(second_score, 100)
    third_score = min(third_score, 100)

    # -----------------------------
    # Render Result Page
    # -----------------------------
    return render_template(
        'result.html',
        name=name,
        age=age,
        gender=gender,
        institution=institution,
        education_level=education_level,
        score_value=score_value,
        career=best_career,
        score=best_score,
        second_career=second_career,
        second_score=second_score,
        third_career=third_career,
        third_score=third_score,
        subjects=subjects,
        skills=skills,
        interest=interest,
        work_style=work_style,
        career_goal=career_goal,
        hobbies=hobbies
    )


# Run App
if __name__ == '__main__':
    app.run(debug=True)
