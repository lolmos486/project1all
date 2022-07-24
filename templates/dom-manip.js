let usn = document.getElementById('password');
let pwd = document.getElementById('password');


let submitButton = document.getElementById('submit')
submitButton.addEventListener('click', )


fetch('127.0.0.1:8080/login', 
    'method': 'POST',
    'headers': {
        'Content-Type': 'application/json'
    },
    'body': JSON.stringify ({
        "username": usn.value,
        "password": pwd.value
    }));

