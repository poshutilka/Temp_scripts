class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    def answer_question(self, question):
        print(f'Очень интересный вопрос! Не знаю.')


class Student(Human):
    def __init__(self, name, someone=None, question=None):
        super().__init__(name)
        self.someone = someone
        self.question = question
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос; 
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        # напечатайте на экран вопрос в нужном формате
        print(f'{self.someone}, {self.question}')
        # запросите ответ на вопрос у someone
        super().answer_question(question)
        print()  # этот print выводит разделительную пустую строку	


class Curator(Human):
    def __init__(self, question):
        self.question = question

    def answer_question(self, question):
              if question == 'мне грустненько, что делать':
                  print(f'Держись, всё получится. Хочешь видео с котиками?')
              return super().answer_question(question)
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса

# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def __init__(self, question):
        self.question = question

    def answer_question(self, question):
              if question == 'что не так с моим проектом?':
                  print(f'О, вопрос про проект, это я люблю.')
              return super().answer_question(question)
              
class Mentor(Human):
    def __init__(self, question):
        self.question = question
        
    def answer_question(self, question):
              if question == 'мне грустненько, что делать?':
                  print(f'Отдохни и возвращайся с вопросами по теории.')
              elif question == 'как устроиться на работу питонистом?':
                  print(f'Сейчас расскажу.')
              return super().answer_question(question)

# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')