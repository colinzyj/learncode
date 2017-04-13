$(document).ready(function(){
      $('#bt1').bind('click',function(){
         $('#ctx').hide(600);
      });
      $('.bt2_class').bind('click',function(){
        $('#ctx').show(100);
      });      
	 
      //$('#ctx2').hide()
      $('#hbt1').on('click',function(){
        $('#ctx1').hide(100)
        $('#ctx2').show(100)
      });
      $('#hbt2').on('click',function(){
        $('#ctx2').hide(100)
        $('#ctx1').show(100)
      });
    });  