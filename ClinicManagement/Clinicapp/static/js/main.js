function pay() {
    fetch('/api/pay', {
        method: 'post',
        headers: {
            'Context-Type': 'application/json'
        }
    }).then(res => res.json()).then(data => {
        alert(data.message);
        location.reload();
    }).catch(err => {
        location.href = '/admin?next=/payment';
    });
}