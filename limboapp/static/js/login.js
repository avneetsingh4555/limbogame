$(document).ready(function(){
    $('.loginbtn').click(function(){
      
      var user = $('.uname').val();
      var pass = $('.upass').val();
      if(user == "" && pass == ""){
       
        alert("** the username and password must be filled **");
        return false;
      }
      if(user == ""){
       
        alert("** the username must be filled **");
        return false;
      }
      if((user.length <=2) || (user.length >=26)){
      
        alert("** the username must be between 3 and 25 letters");
        return false;
      }
      if(pass == ""){
       
        alert("** the password must be filled **");
        return false;
      }
      if((pass.length <=8)){
      
        alert("** the password must be greater than 8");
        return false;
      }
    })
  })