import requests
from bs4 import BeautifulSoup

jogadores_lista = []
for i in range(1, 21):
    print(f'buscando página {i}')
    print("buscando jogadores...")
    if i == 1:
        url = "https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/torschuetzenliste/wettbewerb/BRA1/ajax/yw1/saison_id/0/detailpos//altersklasse/alle/plus/1"
    else:
        url = f"https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/torschuetzenliste/wettbewerb/BRA1/ajax/yw1/saison_id/0/detailpos//altersklasse/alle/plus/1/page/{i}"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, "html.parser")

    linhas_jogadores = soup.find_all("tr", {"class": ["odd", "even"]})

    for linha in linhas_jogadores:
        nome = linha.find("table", {"class": "inline-table"}).text.strip()
        gols = linha.find_all("td")[14].text.strip()
        assistencias = linha.find_all("td")[9].text.strip()
        qtd_jogos = linha.find_all("td")[8].text.strip()
        
        jogadores_lista.append({
            "nome": nome,
            "gols": int(gols) if gols.isdigit() else 0,
            "assistencias": int(assistencias) if assistencias.isdigit() else 0,
            "qtd_jogos": int(qtd_jogos) if qtd_jogos.isdigit() else 0
        })

def calcular_pontuacao(jogador):
    if jogador['qtd_jogos'] > 0:
        return ((jogador['gols'] * 3) + (jogador['assistencias'] * 2)) / jogador['qtd_jogos']
    return 0

for jogador in jogadores_lista:
    jogador['pontuacao'] = calcular_pontuacao(jogador)

def merge_sort(jogadores):
    if len(jogadores) > 1:
        meio = len(jogadores) // 2
        esquerda = jogadores[:meio]
        direita = jogadores[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i]['pontuacao'] > direita[j]['pontuacao']:
                jogadores[k] = esquerda[i]
                i += 1
            else:
                jogadores[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            jogadores[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            jogadores[k] = direita[j]
            j += 1
            k += 1

merge_sort(jogadores_lista)

for jogador in jogadores_lista:
    print(f"Nome: {jogador['nome']}, Gols: {jogador['gols']}, Assistências: {jogador['assistencias']}, Quantidade de jogos: {jogador['qtd_jogos']}, Pontuação: {jogador['pontuacao']:.2f}")

with open('jogadores_formatados.txt', 'w', encoding='utf-8') as arquivo:
    for jogador in jogadores_lista:
        dados_formatados = (f"Nome: {jogador['nome']}, Gols: {jogador['gols']}, Assistências: {jogador['assistencias']}, Quantidade de jogos: {jogador['qtd_jogos']}, Pontuação: {jogador['pontuacao']:.2f}\n\n")
        arquivo.write(dados_formatados)
