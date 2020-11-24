function sendRequest2(url,method,data){
    var r  = axios({
        method: method,
        url: url,
        data: data,
        headers: {
            'X-CSRFToken' : '{{csrf_token}}',
            'Content-Type' : 'application/json'
        }
    })
}