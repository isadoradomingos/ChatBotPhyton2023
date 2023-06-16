frases = {
    'inventario_insuficiente': 'Sem os recursos necessários para avançar.',
    'canal_privado': 'Por favor, envie mensagens para mim através de canal compartilhado de texto (não pvt).',
    'sem_canal_de_voz': 'Por favor, esteja em um canal de voz para ter a imersão necessária do jogo.',
    'erro': 'I\'m sorry Dave, I\'m afraid I can\'t do that.'
}

estados = {
    0: {
        'frases': ['Digite "iniciar" para começar o jogo.'],
        'proximos_estados': {
            '[iI]niciar?': 1
        }
    },
    1: {
        'frases': ['Olá|!', 'Tudo bem,|como vai?'],
        'proximos_estados': {
            '[sS](i)+m': 2,
            '[nN][aã]+o': 3
        },
        'inventario': {}
    },
    2: {
        'frases': ['Era uma vez...', 'E lá de volta|outra vez...'],
        'proximos_estados': {
            '[nN][aã]+o': 3
        },
        'inventario': {}
    },
    3: {
        'frases': ['Fim do jogo!', 'Parabéns!'],
        'proximos_estados': {
            '[rR]einiciar?': 1
        },
        'inventario': {}
    }
}

partidas = {}
