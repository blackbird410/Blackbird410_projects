class Question:

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


def cr_qcm():
    """
    This function create a list of questions(qcm) and save them into a text file.
    :return: The name of the file
    """

    print("VOUS ALLEZ CREER UN QUESTIONNAIRE.")
    n_questions = int(input("Entrer le nombre de question : "))
    name = str(input("Saisir le nom du fichier a creer : ")) + ".txt"
    q = open(name, "a")
    for i in range(n_questions):
        q.write(str(i+1) + ".- " + input("Question " + str(i+1) + " : ") + "\n")
        for j in range(3):
            q.write(str(j+1) + ") " + input("OPTION " + str(j+1) + " : ") + "\n")
    q.close()
    return name


def read_qcm(qcm_name):
    """
    This function is here to read the content of a file.
    :param qcm_name: name of the file
    :return: Nothing
    """

    print("___________QCM___________\n")
    q = open(qcm_name, "r")
    for x in q.readlines():
        print(x)
    q.close()


def ass_qcm(qcm_name):
    """
    This function is used to assemble the different questions and answers from a text file into one string.
    These strings will be contained into a list.

    :param qcm_name: str type
    :return: list type
    """

    q_prompts = []
    q_prompt = ""
    i = 0
    q = open(qcm_name, "r")
    for x in q.readlines():
        if x != "\n":
            if "1)" in x:
                x = "a" + x[1:len(x)]
            elif "2)" in x:
                x = "b" + x[1:len(x)]
            else:
                if "3)" in x:
                    x = "c" + x[1:len(x)]
            q_prompt += x
            i += 1
            if i == 4:
                q_prompts.append(q_prompt)
                q_prompt = ""
                i = 0
        q.close()
    return q_prompts


def correct_qcm(questions):
    """
    This function is here to save the correct answers to a qcm file.
    In other words it's here to return a correctly answered qcm.
    :param questions: A list of questions
    :return: The name of the file containing the answers
    """

    print("VOUS ALLEZ CORRIGER LE QCM.\n")
    name = str(input("Saisir le nom du fichier a creer : ")) + ".txt"
    answers = open(name, "a")
    for x in questions:
        print(x)
        answers.write(input("RIGHT ANSWER : ") + "\n")
    answers.close()
    print("QCM CORRECTED...\n")
    return name


def qcm_link(q_pr, ans):
    """
    This function is here to link the right answers to the questions in order to run the test.
    :param q_pr: A list of question prompts.
    :param ans: The name of the file containing the correct answers.
    :return: A list containing both questions and answers.
    """

    a = open(ans, "r")
    qcm = []
    for i in range(len(q_pr)):
        qcm.append(Question(q_pr[i], a.readline()[0:1]))
    a.close()
    return qcm


def run_test(questions):
    print("--------RUNNING THE TEST------\n")
    score = 0
    for question in questions:
        answer = input(question.prompt + "VOTRE REPONSE : ")
        if answer == question.answer:
            score += 1
    if score == 0:
        print("\n___________________________________________\nDesole vous n'avez eu aucune bonne reponse !\n")
    else:
        print("\n_____________________________________\nVous avez eu {}/{} reponses correctes !"
              "\n".format(score, len(questions)))


def run_qcm():
    print("BIENVENUE DANS MON QCM !\n")
    x = 2
    while x > 1 or x < 0:
        x = int(input("Voulez-vous creer votre propre qcm ?\n0) OUI\t1) NON\n"))
    if x:
        ques_list = ass_qcm("Ques.txt")
        qc = qcm_link(ques_list, "a.txt")
        run_test(qc)
    else:
        f_name = cr_qcm()
        c = 2
        while c > 1 or c < 0:
            c = int(input("Voulez vous afficher votre QCM ?\n0) OUI\t1) NON\n"))
        if not c:
            read_qcm(f_name)
        ques_list = ass_qcm(f_name)
        qc = qcm_link(ques_list, correct_qcm(ques_list))
        run_test(qc)

run_qcm()
