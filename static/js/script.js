$(document).ready(function() {
    // Fungsi untuk auto-complete kota menggunakan API OpenWeatherMap
    $("#city").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "https://api.openweathermap.org/data/2.5/find",
                dataType: "json",
                data: {
                    q: request.term,
                    type: "like",
                    sort: "population",
                    cnt: 10,
                    appid: "0de6db3e34d0e06246107840671f0c60" // API Key OpenWeatherMap Anda
                },
                success: function(data) {
                    response($.map(data.list, function(item) {
                        return {
                            label: item.name + ", " + item.sys.country, // Menampilkan nama kota dan negara
                            value: item.name
                        };
                    }));
                }
            });
        },
        minLength: 1, // Menunggu pengguna mengetik minimal 3 karakter sebelum menampilkan saran
        select: function(event, ui) {
            $('#city').val(ui.item.value); // Menampilkan nama kota yang dipilih pada input field
        }
    });
});
