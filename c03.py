# Quiz game
# Written by Nachiketh Prabhu
# Run this working starter, then follow Tasks 1–4 in c03.md.

# ==> Task 1 - Add more questions
# Keep each answer in the same position as its question, using lowercase text.
questions = [
    'What is the capital of France?',
    'How many legs does an insect have?',
    'Who wrote \'The Lord of the Rings\'?'
]

answers = [
    'paris',
    '6',
    'j.r.r. tolkien'
]

# ==> Task 2 - Add a welcome message here, before asking a question.
# ==> Task 3 - Create a score variable here, starting at zero.

# ==> Task 4 - Use a loop to ask every question and check its matching answer.
# Lists start at position 0. Replace both [0]s with your loop variable.
answer = input(questions[0] + ' ').lower()

if answer == answers[0]:
    print('Correct!')
    # ==> Task 3 - Increase the score here when the answer is correct.
else:
    print('Wrong!')

# ==> Tasks 2 and 3 - Add a goodbye message and show the score here.
# When you add the loop, keep these final messages outside it.
