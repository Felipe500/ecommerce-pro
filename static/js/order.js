$(document).ready(function(){
    $("form_create_order").submit(function(e){
        e.preventDefault();
    });
}

function order_create(url){
    $.ajax({
        method: "POST",
        url: url,
        data: $('#form_create_order').serialize(),

        success: function (data) {
            if (data.created) {
                console.log("atualizado com sucesso!");
            } else {
                console.log("error ao cadastrar!");
            }
        }
     });
}