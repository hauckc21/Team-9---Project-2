// API key (MapBox default public token)
const API_KEY = "pk.eyJ1IjoiY29sbGVlbjU0NyIsImEiOiJja2Z5YzFrc2ExbDBpMzFxcWc4NHpsZ2ZtIn0.etuB1olIeSofH9wCvn6aPA";

// source = "/static/data/countries.geojson"
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
    center: [40.7, -94.5],
    zoom: 2,
    layers: [grayMap, satelliteMap, outdoorsMap]
});
grayMap.addTo(myMap);

// =====================================================

// Create Country (formerly Earthquake) variables
var countries=new L.LayerGroup();

// Variable Overlays
var overlaysMap={
    "Countries":countries
};
// Add a Control to the Map
L.control.layers(base_map,overlaysMap).addTo(myMap);

source = "/static/data/locations.json"(source,function(countryData)
{
    console.log(countryData.features)
// =====================================================

// Set Marker Color Based on Earthquake Magnitude
// function getColor(mag) {
//     if (mag >= 5) {
//         return "rgb(240, 107, 107)" 
//     } else {
//         if (mag > 4) {
//             return "rgb(240, 167, 107)"
//         } else {
//             if (mag > 3) {
//                 return "rgb(243, 186, 77)"
//             } else {
//                 if (mag > 2) {
//                     return "rgb(243, 219, 77)"
//                 } else {
//                     if (mag > 1) {
//                         return "rgb(226, 243, 77)"
//                     } else {
//                         return "rgb(183, 243, 77)"
//                     }
//                 }
//             }
//         }
//     }
// };

// // Set Marker Size
// function markerSize(mag) {
//     if (mag===0){
//         return 1;
//     }
    
//     return mag*4;
// }

// function marker (features){
//     return{
//         fillOpacity:1,
//         opacity:1,
//         weight: 0.6,
//         fillColor: getColor(features.properties.mag),
//         color: "black",
//         stroke: true,
//         radius: markerSize(features.properties.mag)

//     };
// }
// L.geoJson(countryData,{
//     pointToLayer:function(features,latlng){
//         return L.circleMarker(latlng);
//     },
//     style: marker,
//     onEachFeature: function(features, layer){
//         layer.bindPopup("<h4>"+"Magnitude:"+features.properties.mag+"<br>Location:"+features.properties.place+"</h4>");
//     }
// }).addTo(myMap);

    // Create Map Legend
    // var legend=L.control({position:"bottomright"});
    // legend.onAdd=function (){
    //     var div=L.DomUtil.create("div","info legend");
    //     var colorLabels=[1, 2, 3, 4, 5, 6];
    //     var colors=["lightgreen","yellow","orange","orangered","red","darkred"];
        
    //     // Loop Through and Generate Labels with Colors
    //     for (var i=0;i<colorLabels.length;i++){
    //     div.innerHTML+="<i style='background:"+colors[i]+"'></i>"+colorLabels[i]+
    //     (colorLabels[i+1] ? "&ndash;"+colorLabels[i+1]+"<br>":"+");
    // }
    // return div;
    // };
    // legend.addTo(myMap);

    });