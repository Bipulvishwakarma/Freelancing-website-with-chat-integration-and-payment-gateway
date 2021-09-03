var updateBtns=document.getElementsByClassName('update-cart')

for(var i=0;i<updateBtns.length ;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId=this.dataset.product
        var action=this.dataset.action
        console.log('productId:',productId, 'action:',action)

        console.log('USER:',user)
        if (user==='AnonymousUser'){
            console.log('User is not logged in..')
        }else{
            updateUserOrder(productId,action)    
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in ,sending Data')

    var url='/updateItem/'

    fetch(url,{
        method:"POST",
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})

    })
    .then((response)=>{
        if (!response.ok) {
            // error processing
            throw 'Error';
        }
        return response.json()
    })

    .then((data)=>{
        location.reload()
    });
}


