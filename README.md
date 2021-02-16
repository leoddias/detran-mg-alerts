# detran-mg-alerts

## Como executar - Docker
- Necessário: docker & docker-compose
- Criar um arquivo .env (baseado em .env_example)
- docker-compose up --build -d

consulta-multa: Idle = 3MB RAM | Running < 30MB RAM

Sera executado assim que o container estiver up, e todos os dias as 13:00 (GMT-3)

## Como executar localmente
```bash
pip3 install virtualenv
python3 -m venv detranenv
source detranenv/bin/activate
pip3 install -r requirements.txt
python3 src/main.py PLACA RENAVAM
```
