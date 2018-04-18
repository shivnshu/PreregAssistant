$(document).ready(function(){
	var i=0;
	$("#add_row").click(function(){
	var course = $('#sel').val();
	
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", "/course_detail?num="+course, false );
	xmlHttp.send( null );
	//alert(xmlHttp.responseText);
	details = JSON.parse(xmlHttp.responseText);

	$('#addr'+i).html("<td>" + details.course_num + "</td> <td>" + details.course_name + "</td> <td>" + details.instructor + "</td> <td>" + details.credits +"</td> <td>" + details.timings + "</td> <td><button type='button' class='btn btn-danger delete_row' value='#addr" + i + "'>X</button></td>");

	$('#tab_logic').append('<tr id="addr'+(i+1)+'"></tr>');
		i++; 
	});

	$(document).on('click','.delete_row',function(){		
		var fired_button = $(this).val();
		//alert(fired_button);
		$(fired_button).html('');
	});

});
