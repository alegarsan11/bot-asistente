print("\n User-Accounts \n")

 ## Creacion de user-account
for i in range(0,27):
    if(i == 0):
        print("key,enabled,identity,password,username")
        continue
    if(i<10):
        print('user-account-assistant-0'+str(i).format(2)+',true,"UserIdentity{name: '+"'Alejandro'"+', surname: '+"'Garcia'" +', email: '+"'assistant1@acme.com'"+'}",assistant'+str(i)+',assistant'+str(i))
        continue
    print('user-account-assistant-'+str(i).format(2)+',true,"UserIdentity{name: '+"'Alejandro'"+', surname: '+"'Garcia'" +', email: '+"'assistant1@acme.com'"+'}",assistant'+str(i)+',assistant'+str(i))
    
print("\n Assistants \n")

#Creacion de los assistant (Has de modificar alguno comprobando los limites de cada atributo)
for i in range(0,27):
    if(i == 0):
        print("key,supervisor,expertise_fields,resume,further_information_link,key:userAccount")
        continue
    if(i%2==1):
        if(i<10):
            print('assistant-0'+str(i)+',Asistente numero 1,"Organizado, Trabajador",El mejor asistente,null,user-account-assistant-01')
            continue
        print('assistant-'+str(i)+',Asistente numero 1,"Organizado, Trabajador",El mejor asistente,null,user-account-assistant-01')
    else:
        if(i<10):
            print('assistant-0'+str(i)+',Asistente numero 1,"Organizado, Trabajador",El mejor asistente,https://github.com/Alejandrocg024/Acme-L3-D02,user-account-assistant-02')
            continue
        print('assistant-'+str(i)+',Asistente numero 1,"Organizado, Trabajador",El mejor asistente,https://github.com/Alejandrocg024/Acme-L3-D02,user-account-assistant-02')

print("\n Tutorials \n")
#Creacion de los Tutorials (Has de modificar alguno comprobando los limites de cada atributo)
for i in range(0,27):
    if(i == 0):
        print("key,code,title,sumary,goal,draftMode,key:course,key:assistant")
        continue
    if(i%2==1):
        if(i<10):
            print('tutorial-0'+str(i)+',AA9'+str(i+19)+',Tutorial de prueba,Realizado primer tutorial de prueba,"Aprender ,concentrarse",false,course-02,assistant-01')
            continue
        print('tutorial-'+str(i)+',A9'+str(i+27)+',Tutorial de prueba,Realizado primer tutorial de prueba,"Aprender ,concentrarse",false,course-02,assistant-01')
    else:
        if(i<10):
            print('tutorial-0'+str(i)+',AA9'+str(i+50)+',Tutorial de prueba,Realizado primer tutorial de prueba,"Aprender ,concentrarse",false,course-01,assistant-02')
            continue
        print('tutorial-'+str(i)+',A9'+str(i+31)+',Tutorial de prueba,Realizado primer tutorial de prueba,"Aprender ,concentrarse",false,course-01,assistant-02')

print("\n TutorialSessions \n")
#Creacion de los Tutorials (Has de modificar alguno comprobando los limites de cada atributo)
for i in range(0,27):
    if(i == 0):
        print("key,title,sumary,type_session,start_period,end_period,further_information_link,key:tutorial")
        continue
    if(i%2==1):
        if(i<10):
            print('tutorial-session-0'+str(i)+',Sesion numero 1,Primera sesion del tutorial,BALANCED,2020/1/1 11:20,2020/1/1 11:22,null,tutorial-01')
            continue
        print('tutorial-session-'+str(i)+',Sesion numero 1,Primera sesion del tutorial,BALANCED,2020/1/1 11:20,2020/1/1 11:22,null,tutorial-01')
    else:
        if(i<10):
            print('tutorial-session-0'+str(i)+',Sesion numero 1,Primera sesion del tutorial,BALANCED,2020/1/1 11:20,2020/1/1 11:22,null,tutorial-02')
            continue
        print('tutorial-session-'+str(i)+',Sesion numero 1,Primera sesion del tutorial,BALANCED,2020/1/1 11:20,2020/1/1 11:22,null,tutorial-02')
