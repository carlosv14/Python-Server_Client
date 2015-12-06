class User:

    def __init__(self,username='', name= '', email='', id='',f_nac ='', foto=''):
        self.username = username
        self.name= name
        self.email = email
        self.id = id
        self.f_nac = f_nac
        self.foto = foto

    @staticmethod
    def show(u):
       return str.encode('Nombre: '+ u.name + '\n' + 'User name: '+ u.username +  '\n' + 'Email: '+ u.email + '\n' +'ID: '+  u.id + '\n' +'Birth Date: ' +u.f_nac +'\n' + 'Picture: ' +u.foto)


    @staticmethod
    def emailParse(u):
        return str.encode('<p>Nombre: '+ u.name + '</p>' + '<p>User name: '+ u.username +  '</p>' + '<p>Email: '+ u.email + '</p>' +'<p>ID: '+  u.id + '</p>' +'<p>Birth Date: ' +u.f_nac +'</p>' + '<p>Picture: ' +u.foto+ ":" +'</p>')

    @staticmethod
    def imgSource(u):
        return str.encode(u.foto)