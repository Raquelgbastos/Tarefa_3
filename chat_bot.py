import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()
    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'como te chamas': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        ('hobbies', 'passatempo'): 'Meu hobby é processar informações e conversar!',
        'filme favorito': 'Como sou um programa, não assisto filmes, mas adoro "O Código Matrix"!',
        'comida favorita': 'Minha comida favorita são dados binários!',
        ('quem és', 'o que és'): 'Sou um chatbot, um programa de computador para conversar e ajudar.',
        'tua origem': 'Fui criado para interagir e auxiliar as pessoas.',
        ('desporto', 'futebol'): 'Torço para a seleção de processadores!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'horas': f'São: {datetime.now():%H:%M} horas',
        'data': f'Hoje é dia: {datetime.now():%d-%m-%Y}'
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta


    
    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('\033[1;35mBem-vindo ao ChatBot!\033[m')
    print('\033[1;35mEscreva "bye" para sair do chat\033[m')
    name: str = input('\033[1;35mBot: Como te chamas?\033[m ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
