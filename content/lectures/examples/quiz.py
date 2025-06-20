class Answer:
  def is_correct(self):
    return False

class FreeTextAnswer(Answer):
  """
  >>> ans1 = FreeTextAnswer("Milkweed", False)
  >>> ans1.is_correct("milkweed")
  True
  >>> ans1.is_correct("thistle")
  False
  >>> ans1.display()
  Type your answer in (don't worry about capitalization):
  >>> ans2 = FreeTextAnswer("Armeria Maritima", True)
  >>> ans2.is_correct("armeria maritima")
  False
  >>> ans2.is_correct("Armeria Maritima")
  True
  >>> ans2.display()
  Type your answer in (capitalization matters!):
  """
  def __init__(self, correct_answer, case_sensitive):
    # YOUR CODE HERE
    self.correct_answer = correct_answer
    self.case_sensitive = case_sensitive

  def is_correct(self, user_answer):
    # YOUR CODE HERE
    if not self.case_sensitive:
      return user_answer.lower() == self.correct_answer.lower()
    return user_answer == self.correct_answer

  def display(self):
    # YOUR CODE HERE
    if self.case_sensitive:
      print("Type your answer in (capitalization matters!):")
    else:
      print("Type your answer in (don't worry about capitalization):")


class MultipleChoiceAnswer(Answer):
  """
  >>> ans = MultipleChoiceAnswer("Dill", ["Milkweed", "Dill", "Thistle"])
  >>> ans.is_correct(1)
  False
  >>> ans.is_correct(2)
  True
  >>> ans.is_correct(3)
  False
  >>> ans.is_correct('2') # Handles strings
  True
  >>> ans.display()
  Type the number corresponding to the correct answer.
  1. Milkweed
  2. Dill
  3. Thistle
  """
  # YOUR CODE HERE
  def __init__(self, correct_answer, choices):
    self.choices = choices
    self.correct_answer = correct_answer

  def is_correct(self, user_answer):
    """Assumes user answer is number corresponding to answer."""
    return self.choices[int(user_answer) - 1] == self.correct_answer

  def display(self):
    print("Type the number corresponding to the correct answer.")
    for i in range(0, len(self.choices)):
      print(f"{i + 1}. {self.choices[i]}")



class Question:
  """
  >>> q1 = Question("What plant do Swallowtail caterpillars eat?",
  ...              MultipleChoiceAnswer("Dill", ["Milkweed", "Dill", "Thistle"]))
  >>> q1.prompt
  'What plant do Swallowtail caterpillars eat?'
  >>> q1.answer.correct_answer
  'Dill'
  >>> q1.answer_status
  'unanswered'
  >>> q2 = Question("What plant do Monarch caterpillars eat?",
  ...              FreeTextAnswer("Milkweed", False))
  >>> q2.prompt
  'What plant do Monarch caterpillars eat?'
  >>> q2.answer.correct_answer
  'Milkweed'
  """
  def __init__(self, prompt, answer):
    # YOUR CODE HERE
    self.prompt = prompt
    self.answer = answer
    self.answer_status = 'unanswered'

  def display(self):
    # YOUR CODE HERE
    # Print the question prompt
    print(self.prompt)
    # Display the answer
    self.answer.display()
    # Ask the user for input and store their answer
    user_answer = input()
    # If answer is correct,
    #  display a message congratulating them
    #  and mark answered_correctly instance variable as True
    # If answer is not correct,
    #  display a message showing them correct answer
    #  and mark answered_incorrectly instance variable as False
    if self.answer.is_correct(user_answer):
      print("You got it!")
      self.answer_status = 'correct'
    else:
      print(f"Sorry, it was: {self.answer.correct_answer}")
      self.answer_status = 'incorrect'

class Quiz:
  """
  >>> quiz = Quiz("Butterflies", [])
  >>> quiz.name
  'Butterflies'
  >>> quiz.questions
  []
  >>> q1 = Question("What plant do Swallowtail caterpillars eat?",
  ...              MultipleChoiceAnswer(["Thistle", "Milkweed", "Dill"], "Dill"))
  >>> q2 = Question("What plant do Monarch caterpillars eat?",
  ...              FreeTextAnswer("Milkweed", False))
  >>> quiz.add_question(q1)
  >>> quiz.add_question(q2)
  >>> quiz.questions[0].prompt
  'What plant do Swallowtail caterpillars eat?'
  >>> quiz.questions[1].prompt
  'What plant do Monarch caterpillars eat?'
  """
  def __init__(self, name, questions):
    self.name = name
    self.questions = questions
  
  def add_question(self, question):
    self.questions.append(question)

  def display(self):
    # Display the quiz name
    print(f"Welcome to the quiz on {self.name}!")
    # Initialize the correct counter to 0
    correct_count = 0
    # Iterate through the questions
    #  Display each question
    #  Increment the correct counter accordingly
    for question in self.questions:
      question.display()
      if question.answer_status == 'correct':
        correct_count += 1
    # Print the ratio of correct/total
    print(f"You got {correct_count}/{len(self.questions)} correct.")

