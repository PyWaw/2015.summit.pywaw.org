var position = [52.223706, 21.015961];
 
function showGoogleMaps() {
 
    var latLng = new google.maps.LatLng(position[0], position[1]);
 
    var mapOptions = {
        zoom: 17,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        center: latLng,
        scrollwheel: false,
        styles: [{"stylers": [{ "hue": "#ffb300" }]}]
    };
 
    map = new google.maps.Map(document.getElementById('map'),
        mapOptions);
 
    marker = new google.maps.Marker({
        position: latLng,
        map: map,
        draggable: false,
        animation: google.maps.Animation.DROP
    });
}
 
google.maps.event.addDomListener(window, 'load', showGoogleMaps);