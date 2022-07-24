
let logoutBtn = document.getElementById('logout');
logoutBtn.addEventListener('click', async (e) => 
    {
        let result = await fetch('http://127.0.0.1:8080/logout', {
            'method': 'POST', 
            'credentials': 'include',
            'headers':{
                'Access-Control-Allow-Origin': '*'
            }
        })
        e.preventDefault();
        if (result.status === 201) {
            window.location.href = "./login.html"

        }
    }
)

const modalBg = document.querySelector('.modal-background');
const modal = document.querySelector('.modal');
const receiptImg = document.getElementById('receipt-img');
var status = null;
var type = null;

const statusMenu = document.querySelector('#status-ddown');
let statusBtn = document.getElementById('status-ddown');
statusBtn.addEventListener('click', () => {
    statusMenu.classList.toggle('is-active');
})

const statDDown = document.querySelectorAll('#status-menu a');

statDDown.forEach((item) => {
    item.addEventListener('click', () => {
        statDDown.forEach(a => a.classList.remove('is-active'));
        item.classList.add('is-active');
        let text = document.createTextNode(`${item.id}`);
        let tag = document.getElementById('status-text');
        tag.innerHTML = '';
        tag.appendChild(text);
        
    })
})

const typeMenu = document.querySelector('#type-ddown');
let typeBtn = document.getElementById('type-ddown');
typeBtn.addEventListener('click', () => {
    typeMenu.classList.toggle('is-active');
})
const typeDDown = document.querySelectorAll('#type-menu a');

typeDDown.forEach((item) => {
    item.addEventListener('click', () => {
        typeDDown.forEach(a => a.classList.remove('is-active'));
        item.classList.add('is-active');
        let text = document.createTextNode(`${item.id}`);
        let tag = document.getElementById('type-text');
        tag.innerHTML = '';
        tag.appendChild(text);
    })
})


let getReimbsBtn = document.querySelector('#fetch-reimbs');
getReimbsBtn.addEventListener('click', getRes);



async function getRes() {    
    try{
        let statuses = document.querySelectorAll('#status-menu a');
        let status;
        for (let choice of statuses) {
            if (choice.classList.contains('is-active')) {
                status = `${choice.id}`;
                break;
            }
        }

        let types = document.querySelectorAll('#type-menu a');
        let type;
        for (let choice of types) {
            if (choice.classList.contains('is-active')) {
                type = `${choice.id}`;
                break;
            }
        }
        
        let getReimbs = await fetch(`http://127.0.0.1:8080/e/reimbursements?filter-status=${status}&filter-type=${type}`, {
                'credentials': 'include',
                'method': 'GET'
        })
        if (getReimbs.status === 201) {
            let reimbsJson = await getReimbs.json();
            addReimbToTable(reimbsJson);
        }
        else if (getReimbs.status === 401) {
            window.location.href = "./login.html"
        }
    } catch (err) {
        console.log(err)
    }
}


function addReimbToTable(reimbs){
    let reimbTable = document.querySelector('#reimbs-table tbody');
    reimbTable.innerHTML = '';
    for (re of reimbs.reimbs) {
        console.log(re);
        let row = document.createElement('tr');
        let idCell = document.createElement('td');
        idCell.innerHTML = re.reimb_id;
        let amountCell = document.createElement('td');
        amountCell.innerHTML = re.amount;
        let status = document.createElement('td');
        status.innerHTML = re.status;
        let type = document.createElement('td');
        type.innerHTML = re.type;
        let descrip = document.createElement('td');
        descrip.innerHTML = re.description;
        let submittedBy = document.createElement('td');
        submittedBy.innerHTML = re.submitter_id;
        let subOn = document.createElement('td');
        subOn.innerHTML = re.date_submitted.slice(0, re.date_submitted.length - 7);
        let receipt = document.createElement('td');
        if (re.receipt != "None") {
            receipt.innerHTML = `<button class="button" name ="receipt-btn" id="${re.receipt}">receipt</button>`;
            console.log(re.receipt)
            receipt.addEventListener('click', (e) => {
                modal.classList.add('is-active')
                fetch(`http://127.0.0.1:8080/get-receipt/${e.target.id}`)
                    .then(response => response.blob())
                    .then(imageBlob => {
                        const imgObjURL = URL.createObjectURL(imageBlob);
                        console.log(imgObjURL);
                        receiptImg.src = imgObjURL
                    })
            })
        }
        else {
            receipt.innerHTML = '';
        }
    
        let resolBy = document.createElement('td');
        resolBy.innerHTML = re.resolver_id;
        let resolOn = document.createElement('td');
        if (re.date_resolved == 'None') {
            resolOn.innerHTML = '';
        }
        else {
            resolOn.innerHTML = re.date_resolved.slice(0, re.date_resolved.length -7);
        }

        row.appendChild(status);
        row.appendChild(idCell);
        row.appendChild(amountCell);
        row.appendChild(type);
        row.appendChild(descrip);
        row.appendChild(submittedBy);
        row.appendChild(subOn);
        row.appendChild(receipt);
        row.appendChild(resolBy);
        row.appendChild(resolOn);

        reimbTable.appendChild(row);

    }
}

getRes();
    

modalBg.addEventListener('click', () => {
    modal.classList.remove('is-active')
    receiptImg.src = '';
 })

