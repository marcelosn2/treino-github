def calcula_investimento(investimento,meses,ativo):
    i=1
    valor=investimento
    if ativo=='CDB':
        while i<=meses:
            valor=valor*(1.013)
            if i%6==0:
                valor=valor*(1.012)
            i+=1
            return(valor)
    elif ativo=='LCI':
        while i<=meses:
            valor=valor*(1.016)
            i+=1
        return(valor)
    elif ativo=='LCA':
        while i<=meses:
            valor=valor*(1.0145)
            if i%4==0:
                valor=valor*(1.01)
            i+=1
        return(valor)
    else:
        return(investimento)    
        
print(calcula_investimento(1000,12,'CDB'))

