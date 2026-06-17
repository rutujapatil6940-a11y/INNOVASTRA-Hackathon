import json
import csv

def calculate_score(candidate):
    score = 0
    exp = candidate['profile'].get('years_of_experience', 0)
    score += exp * 2
    summary = candidate['profile'].get('summary', '').lower()
    skills = ['python', 'sql', 'spark', 'cloud', 'data']
    for skill in skills:
        if skill in summary:
            score += 5
    return score

file_path = '[PUB] India_runs_data_and_ai_challenge/India_runs_data_and_ai_challenge/candidates.jsonl'
candidates = []

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        cand = json.loads(line)
        cand['score'] = calculate_score(cand)
        candidates.append(cand)

# sort according to score
candidates.sort(key=lambda x: x['score'], reverse=True)

# genrrate CSVfile with 100 rows
with open('final_rankings.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['candidate_id', 'rank', 'score', 'reasoning']) # Requirement ke columns
    
    for i in range(1, 101):
        if i <= len(candidates):
            c = candidates[i-1]
            writer.writerow([c['candidate_id'], i, c['score'], 'Qualified based on skill/exp'])
        else:
            writer.writerow(['N/A', i, 0, 'No candidate'])

print("Final 100-row CSV generated!")
