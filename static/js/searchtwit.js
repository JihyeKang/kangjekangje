$(document).ready(function(){
	$('#search').click(function(){
		var text = $('#text').val();
		$.ajax({
			url:'/searchtwit',
			type:'POST',
			data:{"text":text},
			success:function(response){
				$('#list').empty();
				var result = $.parseJSON(response);
				console.log(response);
				var content = "<table>"
				for(var i=0; i<result.length; i++){
					content +='<tr><td>'+result[i]['user']+'</td><td>'+result[i]['text']+'</td></tr>';
				}
				content += "</table>";
				$('#list').append(content);
			},
			error:function(){
				console.log('error');
			},
			complete:function(){
				console.log('complete');
			}
		});
	});
});
