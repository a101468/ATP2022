import csv
import matplotlib.pyplot as plt

def lerAlunos(filename):
    file = open(filename, encoding= "UTF8")
    res = []
    file.readline()
    csv_file = csv.reader(file, delimiter= ",")
    for linha in csv_file:
        dic = {
        "id": linha[0],
        "nome": linha[1],
        "curso": linha[2],
        "tpc1": linha[3],
        "tpc2": linha[4],
        "tpc3": linha[5],
        "tpc4": linha[6],
        }
        res.append(dic)
    file.close()
    return res

def distribCurso(alunos):
    distrib = {}
    for aluno in alunos:
        if aluno["curso"] in distrib.keys():
            distrib[aluno["curso"]] += 1
        else:
            distrib[aluno["curso"]] = 1
    return distrib

def mediaTPC(alunos):
    for aluno in alunos:
        media = (int(aluno["tpc1"]) + int(aluno["tpc2"]) + int(aluno["tpc3"]) + int(aluno["tpc4"]))/4
        dicMedia = {"media": media}
        aluno.update(dicMedia)
    return alunos

def gradeTPC(alunos):
    for aluno in alunos:
        media = float(aluno["media"])
        if media< 5 and media>= 1:
            grade = "E"
            dicGrade = {"escalao": grade}
            aluno.update(dicGrade)
        elif media< 9 and media>= 5:
            grade = "D"
            dicGrade = {"escalao": grade}
            aluno.update(dicGrade)
        elif media< 13 and media>= 9:
            grade = "C"
            dicGrade = {"escalao": grade}
            aluno.update(dicGrade)
        elif media< 17 and media>= 13:
            grade = "B"
            dicGrade = {"escalao": grade}
            aluno.update(dicGrade)
        elif media< 20 and media>= 17:
            grade = "A"
            dicGrade = {"escalao": grade}
            aluno.update(dicGrade)
    return alunos

def distribEscalao(alunos):
    distrib = {}
    for aluno in alunos:
        if aluno["escalao"] in distrib.keys():
            distrib[aluno["escalao"]] += 1
        else:
            distrib[aluno["escalao"]] = 1
    return distrib

def graph(distrib):
    fig1 = plt.figure(figsize = (20, 20))
    plt.bar(distrib.keys(), distrib.values(), color= "purple", width= 0.3)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys())
    plt.title("Gráfico da distribuição")
    plt.ylabel("Num de alunos")
    plt.show()
    return

def pp(distrib):
    for campo in distrib.keys():
        print(f"{campo:^10}|{distrib[campo]:<5}")
    return

def menu():
    print('''\nMenu:
(1) Ver menu
(2) Ver alunos
(3) Média dos alunos
(4) Escalão dos alunos
(5) Distribuições
(6) Gráficos
(0) Sair''')
    return

def submenuDistrib():
    print('''\nSubmenu:
    (1) Ver submenu
    (2) Distribuição por curso
    (3) Distribuição por escalão
    (0) Sair''')
    return

def submenuGraph():
    print('''\nSubmenu:
    (1) Ver submenu
    (2) Gráfico da distribuição por curso
    (3) Gráfico da distribuição por escalão
    (0) Sair''')
    return