import Pyro4

@Pyro4.expose
class GameServer:
    def init(self):
        self.prize = 0 
        self.questions = [] 
        self.load_questions() 

    def load_questions(self):
        self.questions = [
            {
                "question": "No contexto de sistemas distribuídos, o que é a comunicação assíncrona e como ela difere da comunicação síncrona?",
                "answers": [
                    "a) Comunicação assíncrona é mais rápida que a comunicação síncrona.",
                    "b) Comunicação assíncrona envolve a transferência de dados em tempo real, enquanto a comunicação síncrona não.",
                    "c) Comunicação assíncrona permite que os participantes continuem suas tarefas sem esperar uma resposta imediata, ao passo que a comunicação síncrona exige que todos os participantes estejam",
                    "d) Comunicação assíncrona é uma técnica usada apenas em sistemas centralizados."
                ],
                "correct_answer": "C"
            },
            {
                "question": "Quem foi o líder da Revolta da Armada, um conflito ocorrido no final do século XIX no Brasil?",
                "answers": [
                    "a) Marechal Deodoro da Fonseca.",
                    "b) Barão do Rio Branco.",
                    "c) Almirante Custódio de Melo.",
                    "d) Marechal Floriano Peixoto."
                ],
                "correct_answer": "C"
            },
            {
                "question": "Qual evento histórico marcou o início da Era Vargas no Brasil?",
                "answers": [
                    "a) A Proclamação da República.",
                    "b) A Revolução Constitucionalista de 1932.",
                    "c) A Guerra dos Farrapos.",
                    "d) O Golpe de Estado de 1937."
                ],
                "correct_answer": "D"
            },
            {
                "question": "Qual é a principal diferença entre sistemas distribuídos e sistemas centralizados?",
                "answers": [
                    "a) Apenas sistemas distribuídos usam protocolos de rede.",
                    "b) Em sistemas distribuídos, os recursos são compartilhados e executados em várias máquinas.",
                    "c) Sistemas distribuídos são mais rápidos que sistemas centralizados.",
                    "d) Sistemas centralizados são mais seguros do que sistemas distribuídos."
                ],
                "correct_answer": "B"
            },
            {
                "question": "Quem foi o líder do movimento conhecido como 'Inconfidência Mineira', que ocorreu no final do século XVIII e buscava a independência da Capitania de Minas Gerais do domínio português?",
                "answers": [
                    "a) Tiradentes.",
                    "b) Dom Pedro I.",
                    "c) Dom João VI.",
                    "d) Tiririca."
                ],
                "correct_answer": "A"
            }
        ]

    def get_prize(self):
        return self.prize

    def get_question(self, question_number):
        return self.questions[question_number]

    def check_answer(self, question_number, answer):
        correct_answer = self.questions[question_number]["correct_answer"]
        if answer.lower() == correct_answer.lower():
            self.prize += 200000
            return True
        else:
            self.prize /= 2
            return False

daemon = Pyro4.Daemon()
uri = daemon.register(GameServer())
print(f"URI: {uri}")

with Pyro4.locateNS() as ns:
    ns.register("game_server", uri)

print("Servidor aguardando chamadas...")
daemon.requestLoop()