let amount = document.getElementById('amount-input');
let descrip = document.getElementById('descrip-input');
let reimbSubmitBtn = document.getElementById('reimb-submit-btn');
let typeBtns = document.querySelectorAll('input[name="type"]');
let receiptUpload = document.getElementById('receipt')


// let handleImageUpload = event => {
//     let files = event.target.files;
//     let formData = new FormData();
//     formData.append('myFile', files[0]);

//     fetch('/saveImage', {
//         method: 'POST',
//         body, formData
//     })
//     .then(response => response.json())
//     .then(data => {console.log(data.path)})
//     .catch(error => {
//         console.error(error)
//     })
// }

reimbSubmitBtn.addEventListener('click', async (e) => {
    
    try {
        console.log('click');
        let selectedType;
        for (let radioBtn of typeBtns) {
            if (radioBtn.checked){
                selectedType = radioBtn;
                break;
            }
        }
        let receipt = document.getElementById('receipt');
        let formData = new FormData();
        formData.append('amount', amount.value);
        formData.append('description', descrip.value);
        formData.append('type', selectedType.value);
        formData.append('receipt', receipt.files[0]);
        console.log(amount.value);
        console.log(descrip.value);
        console.log(selectedType.value);

        e.preventDefault();


        let result = await fetch('http://127.0.0.1:8080/e/reimbursement', {
            'credentials': 'include',
            'method': 'POST',
            // 'headers': {
            //     'Content-Type': 'multipart/form-data'
            // },
            'body': formData
            // 'form': JSON.stringify({
            //     'amount': amount.value,
            //     'description': descrip.value,
            //     'type': selectedType.value,
            // }),
            // 'files': receipt
        })
        
        if (result.status == 201) {
            window.location.href = './employee-home.html'
        }/*
        else if (res.status == 400) {
            let data = await res.json();
            
            let errorMessagesDiv = document.getElementById('error-messages')
            errorMessagesDiv.innerHTML = '';

            let errMessages = data.messages;
            for (let errorMessage of errMessages) {
                let errorElement = document.createElement('p');
                errorElement.innerHTML = errorMessage;
                errorElement.style.color = 'red';
                errorElement.style.fontWeight = 'bold';

                errorMessagesDiv.appendChild(errorElement);
            }
        }*/
    }
    catch (err) {
        console.log(err);
    }
})