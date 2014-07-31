$(document).ready(function(){
	$('#mainpt').hover(function(){
		$(this).fadeTo(1000,0.5);	
		$('#myModal').modal('toggle');
	});


});