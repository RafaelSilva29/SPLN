#!/usr/bin/env python3
from re import sub, findall
import fileinput
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt
import shelve


#####################################################################################################################
##################################################### Functions #####################################################
#####################################################################################################################

def frases(texto):
    exp = r'(\n\n+\s*)([A-Z])'
    texto = sub(exp, r'\1@\2', texto)
    exp2 = r'([a-z][.?!]+[\s]*)([A-Z])'
    texto = sub(exp2 , r'\1@\2', texto)
    return texto

def marcarNomes(texto):
    maiuscula = r'(?:[A-Z)]\w+(?:[-\']\w+)*|[A-Z]\.|[IVXLCDM]+)'
    s = r'\s+'
    ent = f"([^@\w])({maiuscula}(?:{s}{maiuscula}|{s}{maiuscula})*)"
    texto = sub(ent,r'\1{\2}', texto)
    return texto

def getNomes(texto):
    ent = findall('{.*?}',texto)
    names = []
    for w in ent:
        names.append(w[1:-1])
    return set(names)

def getPares():
    pairs = {}
    for line in fileinput.input():
        tuples = list(combinations(getNomes(marcarNomes(frases(line))),2))
        for pair in tuples:
            sim = (pair[1],pair[0])
            if pairs.get(sim,0) == 0:
                pairs[pair] = pairs.get(pair,0) + 1
            else:
                pairs[sim] = pairs.get(sim,0) + 1
    return pairs

def otimiza():
    trimmedPairs = {}
    for w,v in getPares().items():
        if (v > 4) and (w[0] not in proib) and (w[1] not in proib):
            if (w[0] not in w[1]) and (w[1] not in w[0]):
                trimmedPairs[w] = v
    return trimmedPairs

def numeroAmigos(g,personagem):
    return g.degree[personagem]

def topAmigos(g,personagem,n):
    dic = {}
    for a in list(G.adj[personagem]):
        if (personagem,a) not in listaPares:
            dic[a] = listaPares[(a,personagem)]
        else:
            dic[a] = listaPares[(personagem,a)]
    res = {}
    i = 0
    for a,v in sorted(dic.items(),key= lambda x : x[1],reverse=True):
        if i < n:
            res[a] = v
            i += 1
        else:
            break
    return res

def showGrafoIndividual(G,personagem):
    g = nx.Graph()
    for w,v in G.edges(nbunch=personagem):
        g.add_edge(w, v)
    plt.figure(figsize = (12, 8))
    nx.draw(g, with_labels = True, node_size = 2000, font_size = 10)
    plt.show()
    g.clear()
    
#####################################################################################################################
##################################################### EXECUTING #####################################################
#####################################################################################################################

#DEFINIR PALAVRAS QUE SÃO PROIBIDAS, NAO SAO PERSONAGENS
proib = ['I','Erised','You\'re','We\'ve','Why','Thanks','No','How','All','Come','The','So','Oh','Don\'t','You','He\'s','It','We','He','It\'s','Mr','Mrs','And','Well','What','Yeah','Yes','But','An','Er','That\'s','If','Can\'t','What\'s']
listaPares = otimiza()


with shelve.open("HarryPotterRelations_DB") as hp:
    k = 0
    for i in listaPares:
        hp[str(k)] = { "Name": i[0], "Friend Name": i[1] }
        k += 1
