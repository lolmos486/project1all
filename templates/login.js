//login

let username = document.getElementById('username')
let password = document.getElementById('password')
const modalBg = document.querySelector('.modal-background');
const modal = document.querySelector('.modal');


let loginButton = document.getElementById('login-btn');

loginButton.addEventListener('click', async (e) => {
    console.log("click submit")
    e.preventDefault();

    let result = await fetch('http://127.0.0.1:8080/login', {
        'credentials': 'include',
        'method': 'POST',
        'headers': {
            'Content-type': 'application/json'
        },
        'body': JSON.stringify({
            "username": username.value,
            "password": password.value
        })
    })
    
    let data = result.json()
    

   if (result.status === 200){
        console.log("status 200")

            data.then(value => {
                if (value.role === "finance_manager"){
                    window.location.href = 'finance-manager-home.html'
                }
                else if (value.role === "employee"){
                    window.location.href = 'employee-home.html'
                }

            })
     //   if 
        
           // window.location.href = 'home.html'
       
    }
    else if (result.status === 400) {
        let regErrorMessages = document.getElementById('reg-error-msgs')
        modal.classList.add('is-active')
        data.then(value => {
            regErrorMessages.innerHTML = value.message
            // alert(value.message);
            console.log(data)
            console.log(value.message)
        })
        
    }
    else {
        console.log("problem")
    }
    
});



modalBg.addEventListener('click', () => {
    modal.classList.remove('is-active')
    window.location.href = 'login.html'
 })

