// API key (MapBox default public token)
const API_KEY = "pk.eyJ1IjoiY29sbGVlbjU0NyIsImEiOiJja2Z5YzFrc2ExbDBpMzFxcWc4NHpsZ2ZtIn0.etuB1olIeSofH9wCvn6aPA";

// current alliance info
var selected_countries = country_details.map(country => country.name)

source = "/static/data/locations.json"


var grayMap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/light-v10",
    accessToken: API_KEY
  });
 

  var satelliteMap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/satellite-v9",
    accessToken: API_KEY
  });

  var outdoorsMap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/outdoors-v11",
    accessToken: API_KEY
  });

// Create Base Map
var base_map={
    Grayscale: grayMap,
    Satellite: satelliteMap,
    GlobalBlue:outdoorsMap
};

// Declare Map Object & set it to Map Element in the DOM
var myMap = L.map("mapid",{
    center: [30, 0],
    zoom: 2,
    layers: [grayMap, satelliteMap, outdoorsMap]
});
grayMap.addTo(myMap);

// =====================================================

// Create Country (formerly Earthquake) variables
var countries=new L.LayerGroup();

// Add a Control to the Map
L.control.layers(base_map).addTo(myMap);

source = d3.json(source,function(countryData)
{
  var countries = countryData.map(country => country.CountryName);
  var latitudes = countryData.map(country => country.CapitalLatitude);
  var longitudes = countryData.map(country => country.CapitalLongitude);

  for (i=0; i < countries.length; i++){
    if (selected_countries.includes(countries[i])){
      L.marker([latitudes[i],longitudes[i]]).addTo(myMap);
    }
  }  
});