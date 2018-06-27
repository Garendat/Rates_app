$(document).ready(function() {
var submitButton = null;
var process = 0;
var day = 0;
    function setChart(data){
       var ctx = document.getElementById('myChart').getContext('2d');
                   new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: data.date,
                            datasets: [{
                                label: 'На графике показаны данные по '+ submitButton,
                                data: data.bid,
                                lineTension: 0,
//                                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                                borderColor: '#007bff',
                                borderWidth: 0,
                                pointBackgroundColor: '#007bff'
                            }]
                        },
                         options: {
                            events:[],
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:false
                }
            }]
        }
    }
                    });

                    };


function startInterval(){
       var sampleXX = $.ajax({
            url: "myChart/",
            type: "GET",
                data: {'data': submitButton, 'date': day},
                success: function (data) {
                   setChart(data);
                   }
        });

};
 $('.btn-day').on('click', function(event) {
        day = event.target.id;
        clearInterval(process);
        if (day === 'today' && submitButton != null){
               startInterval();
               process = setInterval(startInterval, 5000);
                }else if (day != 'today' && day != 0 && submitButton != null){
                startInterval();
                }
                                });

$('.btn-rates').on('click', function(event) {
            submitButton  = event.target.id;
            clearInterval(process);
            if (day === 'today'){
            $.ajax({
                url: "myChart/",
                type: "GET",
                data: {'data': submitButton, 'date': day},
                success: function (data) {
                   setChart(data);
                process = setInterval(startInterval, 5000);
                }
                })
                }
            else if (day === "yesterday" || day === 'two_days_ago'){
                $.ajax({
                url: "myChart/",
                type: "GET",
                data: {'data': submitButton, 'date': day},
                success: function (data) {
                   setChart(data);
                   }
                   });
                   }

});
})