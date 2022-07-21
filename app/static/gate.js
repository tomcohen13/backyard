window.setTimeout(function() {
    $(".alert").fadeTo(500, 0) 
}, 5000);




window.onload=function(){
    // console.log("hey");
    $('label[name="action"]').click(function(){
        if($(this).is(":checked")){
          //input element where you put value
          $("#myForm").action = "/auth/" + this.name
          // console.log($("#isClicked").val());              
        }
      });
}