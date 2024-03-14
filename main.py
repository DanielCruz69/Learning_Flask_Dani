from flask import Flask, request, make_response, redirect, render_template 

app = Flask(__name__)

Tasks = ['Todo1', 'Todo2', 'Todo3', 'Todo4' ];
Lenght_Task = len(Tasks);

@app.route('/')
def Making_A_Cookie():

	User_Ip = request.remote_addr;
	Response = make_response(redirect('/Hello'));
	Response.set_cookie("User_ID", User_Ip);
	return Response;

@app.route('/Hello')
def Say_Hello():
	User_Ip = request.cookies.get('User_ID');
	Context = { 'User_Ip': User_Ip,
				 'Tasks': Tasks,
				 'Len': Lenght_Task
			  };
													 #Si no lo quiero utilizar (Y para facilitar el código) creo el diccionario y le agrego ** al inicio para que expanda el diccionario y funcione como si los estuviese nombrando por separado.
	return render_template('Hello.html', **Context); #Si utilizo el context=context en la declaracion html debo utilizar context(Que es la variable en la que guarde las otras "Variables") luego un "." y a continuación debo de agregar la variable o el valor que quiero utilizar Ej: Context.User_Ip --> Esto en el HTML



#if __name__ == '__main__': Esto se realiza con la finalidad de decirle que la app que se llame como el archivo que estamos usando (__name__) ejecute e debug mode automaticamente
    #app.run(debug=True)