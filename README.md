cvrobot - API para o cienciavitae.pt

Modulo Python para inserir dados no cienciavitae.pt. Útil para quem é demasiado
preguiçoso ou tem o CV demasiado grande. Exemplo simples de utilização:

```
#!/usr/bin/env python3

import cvrobot
from cvrobot.util import pedePassword

user = 'me@somewhere.com'
robot = cvrobot.CVRobot(user, pedePassword(user))

a = robot.atividades()
a.arbitragemCientificaEmConf('Intl. Conf. on Click-Happy User Interfacaes', '2016')
a.orientacao('Towards clickable stuff', 'José Alguém', 'Doutoramento', '2015')
```

Neste momento suporta apenas um conjunto muito limitado de atividades, mas
pode facilmente ser melhorado copiando e alterando o código existente.

Aviso: Não me responsabilizo por quaisquer consequências da utilização deste
código! Convém experimentar com casos isolados antes de tentar carregar
grandes quantidades de informação e ficar atento à janela do browser...

Obtenha a última versão e contribua modificações e melhoramentos
aqui: https://github.com/jopereira/cvrobot

