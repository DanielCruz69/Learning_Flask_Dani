from flask import Flask, request, make_response, redirect, render_template, session, current_app, g
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'NO_ADIVINAS_ÑO'


Tasks = ['Daniel', 'Hamet', 'Diego', 'Yudy' ];
Lenght_Task = len(Tasks);

class LoginForm(FlaskForm):

	Username = StringField('Nombre de Usuario', validators = [DataRequired()])
	Password = PasswordField('Contraseña', validators = [DataRequired()])
	Submit = SubmitField('Enviar')


@app.route('/')
def Making_A_Cookie():

	User_Ip = request.remote_addr; #El remote_addr solicita la dirección IP del usuario.
	
	Save_IP_User = make_response(redirect('/Hello'));
	session['User_IP'] = User_Ip

	return Save_IP_User;

@app.route('/Hello', methods=['GET', 'POST'])
def Say_Hello():
	User_Ip = session.get('User_IP');
	Login_Form = LoginForm()
	Username = session.get('Username')


	Context = { 'User_Ip': User_Ip,
				'Tasks': Tasks,
				'Login_Form': Login_Form,
				'Username_Login': Username,
				};
							
	if Login_Form.validate_on_submit():

		Username_Validate = Login_Form.Username.data
		session['Username'] = Username_Validate
							
													 #Si no lo quiero utilizar (Y para facilitar el código) creo el diccionario y le agrego ** al inicio para que expanda el diccionario y funcione como si los estuviese nombrando por separado.
	return render_template('Hello.html', **Context); #Si utilizo el context=context en la declaracion html debo utilizar context(Que es la variable en la que guarde las otras "Variables") luego un "." y a continuación debo de agregar la variable o el valor que quiero utilizar Ej: Context.User_Ip --> Esto en el HTML

@app.route('/Lista')
def Show_Market_List():
	
	return render_template('Lista_Del_Super.html')

@app.errorhandler(404)
def Not_Found_Page(Error):
	return render_template('404.html', Error = Error);

@app.errorhandler(500)
def Server_Error(Error):
	return render_template('500.html', Error = Error);


#Set FLASK_DEBUG=1
#Set FLASK_RUN_PORT=5005

#if __name__ == '__main__': Esto se realiza con la finalidad de decirle que la app que se llame como el archivo que estamos usando (__name__) ejecute e debug mode automaticamente
    #app.run(debug=True)