$(document).ready(function() {
	$(function ($) {
  		$('.spinner .btn:first-of-type').on('click', function() {
    		$('.spinner input').val( parseInt($('.spinner input').val(), 10) + 1);
  		});
  		$('.spinner .btn:last-of-type').on('click', function() {
    		$('.spinner input').val( parseInt($('.spinner input').val(), 10) - 1);
  		});
	});
});

$(document).ready(function() {
    $(function ($) {
        $('.spinner .btn:first-of-type').on('click', function() {
            $('.spinner input').val( parseInt($('.spinner input').val(), 10) + 1);
        });
        $('.spinner .btn:last-of-type').on('click', function() {
            $('.spinner input').val( parseInt($('.spinner input').val(), 10) - 1);
        });
    });
});

function addTask() {
    // $('.ajaxProgress').show();
    $.ajax({
        type: "POST",
        url: "/groupview/add",
        dataType: "json",
        async: true,
        data: {
            csrfmiddlewaretoken = '{{ csrf_token }}'
            taskName: $('#taskName').val()
            taskType: $('#taskType').val()
            description: $('#description').val()
            location: $('#location').val()
            startDateTime: $('#date_timepicker_start').val()
            endDateTime: $('#date_timepicker_end').val()
        }

        success: function(json) {
            $('#output').html(json.message);
            // $('.ajaxProgress').hide();
        }
    });
}

// function addTask() {
//     var taskName = document.getElementById("taskName").value;
//     var taskType = document.getElementById("taskType").value;
//     var descriptionValue = document.getElementById("description").value;
//     var locationValue = document.getElementById("location").value;
//     // var radios = document.getElementsByName("transType");
//     // for (var i = 0, length = radios.length; i < length; i++) {
//     // if (radios[i].checked) {
//     //     var trans= radios[i].value;
//     //     break;
//     // }}
//     var startDateTimeValue = document.getElementById("date_timepicker_start").value;
//     var endDateTimeValue = document.getElementById("date_timepicker_end").value;

//     // if (isNaN(amountValue) == true) {
//     //     alert("amount must be a number!")
//     // }

//     csrfmiddlewaretoken = '{{ csrf_token }}'
//     $.ajax({
//         url : "/groupview/add",
//         type : "POST",
//         data : { method : "add", taskName : taskName, taskType : taskType, description : descriptionValue, 
//                 location : locationValue, date_timepicker_start : startDateTimeValue, 
//                 date_timepicker_end : endDateTimeValue },
//         beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     },
//         success : function(json) {
//             console.log("success");
//             location.reload();
//         }
//     })
// }
