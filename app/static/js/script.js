$(".slider").owlCarousel({
  loop: true,
  autoplay: true,
  autoplayTimeout: 2000, //2000ms = 2s;
  autoplayHoverPause: true,
  items: 7,
  responsive: false,
});

$(document).ready(function(){  
  $('#login_button').click(function(){  
       var username = $('#username').val();  
       var password = $('#password').val();  
       if(username != '' && password != '')  
       {  
            $.ajax({  
                 url:"/login",  
                 method:"POST",  
                 data: {username:username, password:password},  
                 success:function(data)  
                 {  
                      alert(data);  
                      if(data == 'No-data')  
                      {  
                           alert("Неправильний логін чи пароль!");  
                      }  
                      else 
                      {  
                           $('#loginModal').hide();  
                           location.reload();  
                      }  
                 }  
            });  
       }  
       else 
       {  
            alert("Обидва поля обов'язкові!");  
       }  
  });    
});  