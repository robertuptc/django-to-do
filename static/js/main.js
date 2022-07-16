
function logIn(event){
    event.preventDefault()
    email =document.getElementById('email').value
    password = document.getElementById('password').value
    data = {
        'email' : email,
        'password': password,
    }
    console.log(data)
    axios.post('log_in', data)
    .then((response)=>{
        alert(response['data']['Status']);
        window.location.href = 'todos';
    })
}

function signUp(event){
    event.preventDefault()
    email =document.getElementById('email').value
    password = document.getElementById('password').value
    data = {
        'email' : email,
        'password': password,
    }
    axios.post('sign_up', data)
    .then((response)=>{
        console.log('response', response)
    })
}
