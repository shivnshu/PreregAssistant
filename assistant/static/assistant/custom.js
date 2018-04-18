$(document).ready(function(){
	var i=0;
	$("#add_row").click(function(){
	var course = $('#sel').val();
	$('#addr'+i).html("<td>" + course + "</td> <td>" + course + "</td> <td>" + course + "</td> <td>" + course +"</td> <td>" + course + "</td> <td><button type='button' class='btn btn-danger delete_row' value='#addr" + i + "'>X</button></td>");

	$('#tab_logic').append('<tr id="addr'+(i+1)+'"></tr>');
		i++; 
	});

	$(document).on('click','.delete_row',function(){		
		var fired_button = $(this).val();
		//alert(fired_button);
		$(fired_button).html('');
	});

});
