from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Pybot')
bot = ChatBot(
    'Pybot',
    storage_adapter ='chatterbot.storage.SQLStorageAdapter',
    database_uri= 'sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)
conversa.train([
    'Oi?',
    'Olá',
    'Qual  é o seu nome?',
    'Cidpybot',
    'Prazer em te conhecer',
    'Igualmente',
    'Tudo bem?',
    'Muito bem e você?',
    'Ótimo',
    'Você gosta de filmes?',
    'Quais?',
    'Nossa! Ótimo gosto o seu! =)',
    'Papo bom  o nosso',
    'kkkk',
    'adeus',
    'Volte sempre',                
])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.portuguese')

while True:
  resposta = bot.get_response(input("Usuário: "))
  if float(resposta.confidence) > 0.5:
    print("Cidpybot: ", resposta)
  else:
    print("Desculpe, não entendi!")