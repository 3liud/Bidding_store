$(document).ready(function () {
    $.getJSON('/get_bidding_time', {product_id: $('#product_id').val(), view: 'json'}, function (data) {
        sell_on = data['sell_on']
        var today = Date()
        var x = new Date(sell_on);
        var y = new Date(today);
        var bidSeconds = parseInt(data['bid_time']) * 60;
        var newSeconds = bidSeconds;
        resetInterval(x, newSeconds);
    })
});

function resetInterval(x, newSeconds) {
    var bool = true;
    var timer = 0;
    if (bool){
            setInterval(function () {
            var counter = countDown(x);
            var elapsed = counter.elapsed
            counterString =  counter.days + "d "
            + counter.hours + "h " + counter.minutes + "m " + counter.seconds + "s ";
            if (elapsed > 0){
                   $('#countDown').html(counterString);
                   $('#bid_amount').attr('disabled', true);
            }else {
               var zero = '00';
               counterString =  zero + "d "
                + zero + "h " + zero + "m " + zero + "s ";
                $('#countDown').html(counterString);
                $('#bid_amount').attr('disabled', false);

              if (newSeconds <= 0){
                $.getJSON('/reset_bid_time', {product_id: $('#product_id').val(), view: 'json'}, function (data) {
                    $('#bid_amount').attr('disabled', true);

                });
                bool = false;
                    // clearInterval(timer);
                }else {
                    newSeconds = newSeconds - 1;
                    $('#countDown').html(counterString);
                    console.log(newSeconds)
                }
            }
        }, 999);
    }else {
         clearInterval(timer);
    }
}

function  countDown(deadline) {
    var today = Date()
    var y = new Date(today);
    t = deadline - y;
    var days = Math.floor(t / (1000 * 60 * 60 * 24));
    var hours = Math.floor((t % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((t % (1000 * 60)) / 1000);
    return ({'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds, 'elapsed': t});
}
//
// function countdown(deadline) {
//     var deadline = new Date("Jan 5, 2018 15:37:25").getTime();
//     var x = setInterval(function () {
//         var now = new Date().getTime();
//         var t = deadline - now;
//         var days = Math.floor(t / (1000 * 60 * 60 * 24));
//         var hours = Math.floor((t % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//         var minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
//         var seconds = Math.floor((t % (1000 * 60)) / 1000);
//         return (days, hours, minutes, seconds);
// }}