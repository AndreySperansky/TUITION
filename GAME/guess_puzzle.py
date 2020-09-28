def guessPazzle(question, answers):
    #answers = answers[:]
    print("Угадайте загадку: ", question)
    userAnswer = input("Ваш ответ: ")
    userAnswer = userAnswer.lower()

    for i in range(len(answers)):
         if userAnswer == answers[i]:
            print("Это правильный ответ!")
            return
    print("Вы не угадали!")



guessPazzle("Висит груша нельзя скушать?", ("лампа", "лампочка"))
guessPazzle("Белые овечки бегают по свечке?", ["верба", "мимоза"])
guessPazzle("Зимой и летом одним цветом?", ["ель", "елка", "сосна", "кедр"])












