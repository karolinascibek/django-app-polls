from polls.respondents.models import Respondent, Answer, ClosedAnswer, OpenAnswer

# funkcja do zapisania odpowiedzi


def answers_save(respondent, questionnaire, dict):
    for question_id, answers in dict.lists():
        # pobieramy pytania z danej ankiety
        question = questionnaire.question_set.get(pk=question_id)
        # zapisujemy odpowiedzi
        answer = Answer.objects.create(question=question, respondent=respondent)
        if question.type == "single-choice" or question.type == "multiple-choice":
            choices = question.choice_set.filter(pk__in=answers)
            ClosedAnswer.objects.bulk_create(
                [ClosedAnswer(choice=choice, answer=answer) for choice in choices]
            )
        else:
            OpenAnswer.objects.create(answer=answer, contents=answers[0])

