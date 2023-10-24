import Pyro4

uri = "PYRONAME:game_server@localhost:9090"
game_server = Pyro4.Proxy(uri)
game_server.init()

print("Bem-vindo ao Show do Milhão!")
for question_number in range(5):
    print(f"\nPergunta n° {question_number + 1}")
    
    question = game_server.get_question(question_number)
    print(question["question"])
    for answer_option in question["answers"]:
        print(answer_option)

    answer = input("Sua resposta é: ")
    if game_server.check_answer(question_number, answer):
        print("Resposta correta!")
        print(f"Prêmio acumulado em R$ {game_server.get_prize()}")
        if question_number == 4:
            print("\nParabéns, você é o mais novo milionário!")
    else:
        print(f"Resposta incorreta. A alternativa correta era {question['correct_answer']}.")
        print("Fim de jogo! Você receberá metade do prêmio. :(")
        break

print(f"\nTotal do prêmio: R$ {game_server.get_prize()}")