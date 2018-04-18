$(document).ready(function(){
	var i=0;
	localStorage.setItem('courses_list' , '');
	$("#add_row").click(function(){
		var course = $('#sel').val();

		var courses_list = localStorage.getItem('courses_list');
		courses_list = courses_list + " " + course;
		localStorage.setItem('courses_list', courses_list);
		
		var xmlHttp = new XMLHttpRequest();
		xmlHttp.open( "GET", "/course_detail?num="+course+"&courses_list="+courses_list, false );
		xmlHttp.send( null );
		//alert(xmlHttp.responseText);
		details = JSON.parse(xmlHttp.responseText);

		$('#addr'+i).html("<td id='course_num"+i+"'>" + details.course_num + "</td> <td>" + details.course_name + "</td> <td>" + details.instructor + "</td> <td>" + details.credits +"</td> <td>" + details.timings + "</td> <td><button type='button' class='btn btn-danger delete_row' value='" + i + "'>X</button></td>");

		$('#tab_logic').append('<tr id="addr'+(i+1)+'" class="added_courses"></tr>');
		i++;

	});

	$(document).on('click','.delete_row',function(){		
		var fired_button = $(this).val();
		//alert(fired_button);
		var num = $('#course_num'+fired_button).html();
		//alert(num);
		$("#addr"+fired_button).html('');

		var courses_list = localStorage.getItem('courses_list');
		courses_list = courses_list.replace(num, '');
		localStorage.setItem('courses_list', courses_list);
	});

});
