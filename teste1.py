lista = [];

def pega_numeros():
    numero = int(input("Digite um numero:"));
    return numero;

def armazena(numero,lista):
    lista.append(numero);
    return lista;

def ordenaCrescente(lista):
    for x in range(len(lista)):
        for i in range(len(lista)):
            if(lista[x]<lista[i]):
                aux = lista[x];
                lista[x]=lista[i];
                lista[i]=aux;
    return lista

def ordenaDescrescente(lista):
    for x in range(len(lista)):
        for i in range(len(lista)):
            if(lista[x]>lista[i]):
                aux = lista[x];
                lista[x]=lista[i];
                lista[i]=aux;
    return lista

def printa(lista,tipo):
   print("\t","Ordenação ",tipo);
   for x in range(len(lista)):
       print(lista[x]);


for x in range(10):
    armazena(pega_numeros(),lista);
print("Deseja ordenar de forma Crescente ou Decrescente?");
resp = int(input("1- Crescente \n2- Decrescente\n-->"));
if(resp==1):
    printa(ordenaCrescente(lista),"Crescente");
else:
    printa(ordenaDescrescente(lista), "Decrescente");

