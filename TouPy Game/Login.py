def condiçao():
    try:
        global condiçao2
        condiçao2 = int(input('Digite :\n[-1]Para sair do sistema; \n [0] Para se cadastrar e começar a jogar; \n [1] Se já for cadastrado e deseja jogar;\n [2]Para acessar seu histórico de pontuação. \n [3] Para ver o histórico completo. \n Qual opção desejada? '))
        while condiçao2<-1 or condiçao2>3:
            print('\n Valores inválidos. Tente novamente ')
            principal()
    except ValueError:
        print('Digite algo no campo das opções!')
        condiçao()
        
def cond1(condiçao2):
    log = open('login.txt','r')
    
    if condiçao2==1:
        
        login=str(input('Digite seu login: '))
        password=str(input('Digite sua senha: '))
        confirmaçao_dados(login,password,log,condiçao2)
        iniciar_jogo(login,password)
    
    
    log.close()
    
def cond0(condiçao2):

    lerlogin= open('login.txt','r+')
    
    if condiçao2 == 0:
        
        usuario =str(input('Digite um nome de usuário : ' ))
        
        senha = str(input('Digite uma senha: '))
        login=usuario
        password=senha
        confirmar_dados(usuario,senha,lerlogin)
        iniciar_jogo(login,password)
        
        
def confirmar_dados(usuario,senha,lerlogin):
    for linha in lerlogin:
        while usuario in linha:
            print('\n usuário '+usuario+' já existe! ')
            usuario = str(input('Digite outro nome de usuário: '))

        while senha in linha:
            print('\n Senha ',senha,' já existe!')
            senha = str(input('Digite outra senha: '))

    print('\n Dados autorizados! \n')
    gravar_dados(usuario,senha,lerlogin)
    
def gravar_dados(usuario,senha,lerlogin):
    lerlogin.write(usuario + '\n'+ senha + '\n')
    lerlogin.close()
    print('Seu nome de usuário cadastrado é: ', usuario +
          '\n Sua senha cadastrada é: ', senha)
    print('\n Não se esqueça do seu login e senha, pois poderá precisar deles futuramente! ')
    

def cond2(condiçao2):
    log = open('login.txt','r')
    pr=open('pontuação.txt','r')
    if condiçao2==2:
        login=str(input('Digite seu login: '))
        password=str(input('Digite sua senha: '))
        confirmaçao_dados(login,password,log,condiçao2)
        pa=0
        juntos=login+password
        for lis in pr:
            if juntos in lis:
                print("\n Hitórico de pontuação do usuário '"+login +"' é de: "+ lis )
                pa=2
            else:
                pa=pa
        if pa==0:
            print('\n Usuário não tem histórico de pontuação. \n\n')

    log.close()
    pr.close()
    
        
        
def confirmaçao_dados(login,password,log,condiçao2):
    readlist=[]
    f=0
    try:
        for readline in log:
            listaread=readline.strip()
            readlist.append(listaread)
        i1 = readlist.index(login)+1
        ind = readlist[i1]
        i2 = readlist.index(login)-1
        ind2 = readlist[i2]
        if login and password in readlist:
            print('Bem-vindo!\n ')
            
        elif password!=ind:
            print('\n Senha não compatível com login. Tente novamente! ')
            if condiçao2 ==1:
                cond1(condiçao2)
            elif condiçao2 ==2:
                cond2(condiçao2)
            
        elif login!=ind2:
            print('\n Login não compatível com a senha.Tente novamente ')
            if condiçao2 ==1:
                cond1(condiçao2)
            elif condiçao2 ==2:
                cond2(condiçao2)
    except ValueError:
        print('\n Usuário não encontrado!Tente novamente. ')
        if condiçao2 ==1:
            cond1(condiçao2)
        elif condiçao2 ==2:
            cond2(condiçao2)
        f+=1
        if f >2:
            print('\n Você tentou várias vezes, tente outra opção. ')
            condiçao()

 
def iniciar_jogo(login,password):
    p=open('pontuação.txt','a')
    
    jogar = str(input('Deseja começar a jogar? [S]-Sim ou [N]-Não: '))
    
    if jogar =='S' or jogar=='s':
        import jogo
        
    elif jogar=='N' or jogar=='n':
        pass
        
    else:
        print('\n Valores inválidos! \n')
        iniciar_jogo(login,password)
        
    try:
        p.write(login + password +' : '+ str(jogo.score)+'\n')
    except UnboundLocalError:
        pass
    p.close()

def cond3(condiçao2):
    
    L=[]
    j = 0
    L2=[]
    j1= 0
    k1 = 0
    L3=[]
    if condiçao2==3:
        pont = open('pontuação.txt','r')
        print('\n Histórico completo em ordem de pontuação do maior para o menor: \n')
        
        for hc in pont:
            w = hc.strip()
            separando = str.split(w)
            L.append(separando)
        for gg in L:
            a = list(map(int,L[j][2].split(', ')))
            L2.append(a[0])
            L[j].insert(2,a[0])
            del(L[j][3])
            j+=1
          
        L2.sort()
        lista_reduzida= list(set(L2))
        for ss in reversed(lista_reduzida):
            k1=0
            for ss1 in L:
                if ss == L[k1][2]:
                    L3.append(L[k1])
                else:
                    pass
                k1+=1
        if L3==[]:
            print('Histórico de pontuação vazio!')
        else:
            for dd in L3:
                print(dd[0],dd[1],dd[2])
            print()
        
def principal():
    condiçao()
    cond0(condiçao2)
    cond1(condiçao2)
    cond2(condiçao2)
    cond3(condiçao2)
while condiçao!=-1:
    principal()
    if condiçao2==-1:
        exit()




