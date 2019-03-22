$(function () {

    function initMap() {

        var location = new google.maps.LatLng(1.344, 103.839);

        var mapCanvas = document.getElementById('map');
        var mapOptions = {
            center: location,
            zoom: 11,
            panControl: false,
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);

        //var markerImage = new Image();
        //markerImage.src = 'marker.png';

        addMarker({lat:1.41803, lng:103.821}, "PSI North: ", psi_north, 40, 0);//north
        addMarker({lat:1.35735, lng:103.695}, "PSI West: ", psi_west, -50, 50);//west
        addMarker({lat:1.35735, lng:103.821}, "PSI Central: ", psi_central, 0, 50);//central
        addMarker({lat:1.35735, lng:103.941}, "PSI East: ", psi_east, 50, 50);//east
        addMarker({lat:1.29587, lng:103.821}, "PSI South: ", psi_south, 50, 100);//south
        addMarker({lat:1.41803, lng:103.821}, "Weather North: ", weather_north, -50, 0);//north
        addMarker({lat:1.35735, lng:103.695}, "Weather West: ", weather_west, -50, 0);//west
        addMarker({lat:1.35735, lng:103.821}, "Weather Central: ", weather_central, 0, 10);//central
        addMarker({lat:1.35735, lng:103.941}, "Weather East: ", weather_east, 50, 0);//east
        addMarker({lat:1.29587, lng:103.821}, "Weather South: ", weather_south, -50, 100);//south
        
        function addMarker(lat_lng, displayString, region, width, height){
            var marker = new google.maps.Marker({
            position: lat_lng,
            map:map,
            //icon: markerImage
            });
            var contentString = '<div class="info-window">' +
                    '<p>' + displayString + region + '</p>' +
                    '</div>'; 
            var infowindow = new google.maps.InfoWindow({
                content: contentString,
                maxWidth: 160,
                pixelOffset: new google.maps.Size(width,height)
            });
            infowindow.open(map, marker);
        }

        /* var contentString = '<div class="info-window">' +
                '<h3>Info Window Content</h3>' +
                '<div class="info-content">' +
                '<p>Incident Type</p>' +
                '</div>' +
                '</div>';
        var infowindow = new google.maps.InfoWindow({
            content: contentString,
            maxWidth: 400
        });
        marker.addListener('click', function () {
            infowindow.open(map, marker);
        }); */

        //var styles = [{"featureType": "landscape", "stylers": [{"saturation": -100}, {"lightness": 65}, {"visibility": "on"}]}, {"featureType": "poi", "stylers": [{"saturation": -100}, {"lightness": 51}, {"visibility": "simplified"}]}, {"featureType": "road.highway", "stylers": [{"saturation": -100}, {"visibility": "simplified"}]}, {"featureType": "road.arterial", "stylers": [{"saturation": -100}, {"lightness": 30}, {"visibility": "on"}]}, {"featureType": "road.local", "stylers": [{"saturation": -100}, {"lightness": 40}, {"visibility": "on"}]}, {"featureType": "transit", "stylers": [{"saturation": -100}, {"visibility": "simplified"}]}, {"featureType": "administrative.province", "stylers": [{"visibility": "off"}]}, {"featureType": "water", "elementType": "labels", "stylers": [{"visibility": "on"}, {"lightness": -25}, {"saturation": -100}]}, {"featureType": "water", "elementType": "geometry", "stylers": [{"hue": "#ffff00"}, {"lightness": -25}, {"saturation": -97}]}];

        //map.set('styles', styles);
    }
    google.maps.event.addDomListener(window, 'load', initMap);
});