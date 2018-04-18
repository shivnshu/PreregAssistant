$(document).ready(function(){
	var i=0;
	localStorage.setItem('courses_list' , '');


	function refresh_dropdown(){
		var courses_list = localStorage.getItem('courses_list');
		var xmlHttp = new XMLHttpRequest();
		xmlHttp.open( "GET", "/get_non_conflicting_courses?courses_list="+courses_list, false );
		xmlHttp.send( null );
		//alert(xmlHttp.responseText);
		courses_list = JSON.parse(xmlHttp.responseText);
		//alert(courses_list.length);

		var myNode = document.getElementById("sel");
		if (myNode != null){
			while (myNode.firstChild) {
			    myNode.removeChild(myNode.firstChild);
			}
		}

		var i = 0;
		for (i = 0; i < courses_list.length; i++) {
			var select = document.getElementById("sel");
			if (select != null){
				var option = document.createElement("option");
				option.appendChild(document.createTextNode(courses_list[i]));
				select.appendChild(option);
			}
		}
		
	}
	
	refresh_dropdown();

	$("#add_row").click(function(){
		var course = $('#sel').val().split(" ")[0];

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
		
		refresh_dropdown();

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

		refresh_dropdown();
	});


	$("#add_course").click(function(){
		var course_num =  document.getElementById("course_num").value;
		var course_name =  document.getElementById("course_name").value;
		var course_instructor =  document.getElementById("course_instructor").value;
		var course_credits =  document.getElementById("course_credits").value;
		var course_timings =  document.getElementById("course_timings").value;
		//alert(course_num+course_name+course_instructor+course_credits+course_timings);

		var xmlHttp = new XMLHttpRequest();
		xmlHttp.open( "GET", "/course_add?course_num="+course_num+"&course_name="+course_name+"&course_instructor="+course_instructor+"&course_credits="+course_credits+
"&course_timings="+course_timings, false );
		xmlHttp.send( null );

		//console(xmlHttp.responseText);
		window.location.reload();
	});

});
