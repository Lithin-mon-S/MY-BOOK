

function ShowAlert() {

var username=document.getElementById('username').value;
var first_name=document.getElementById('first_name').value;
var last_name=document.getElementById('last_name').value;
var email=document.getElementById('email').value;
var password=document.getElementById('password').value;
var password1=document.getElementById('password1').value;


if ( !username|| !first_name|| !last_name|| !email|| !password|| !password1){

alert('please fill out the required .')

}

else{


alert('Registration successfully. Now you can login ');
}

}