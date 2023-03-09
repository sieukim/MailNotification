function validId(id) {
    if (id.length === 13) {
        return true;
    } else {
        return false;
    }
}

function validUser(user) {
    if (user === '' || !user.match(/^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i)) {
        return false;
    } else {
        return true;
    }
}

function onInput() {
    const id = document.getElementById('id');
    const user = document.getElementById('user');    
    const submit_button = document.getElementById('submit_button');
    if (validId(id.value) && validUser(user.value)) {
        submit_button.disabled = false;
    } else {
        submit_button.disabled = true;
    }
}

async function onClick() {
    const id = document.getElementById('id');
    const user = document.getElementById('user');   
    const dynamo_url = 'https://tnnadjvq5g.execute-api.eu-north-1.amazonaws.com/default/stamp';
    await fetch(dynamo_url+`?id=${id.value}&user=${user.value}`, {
        method: 'POST'
    });
    alert('신청되었습니다.');
    id.value = '';
    user.value = '';
}