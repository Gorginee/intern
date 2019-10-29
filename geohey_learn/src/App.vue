<template>
  <div id="app">
    <div id="mapContainer" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import G from 'geohey-javascript-sdk';
import 'geohey-javascript-sdk/dist/lib/g.css' ;   // 样式
import 'geohey-javascript-sdk/dist/lib/g-canvas.min.js' ;
G.ready(function() { // 此时类库加载完成

    var map = new G.Map('mapContainer');

    var tileLayer = new G.Layer.Tile('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        cluster: ['a', 'b', 'c']
    });
    tileLayer.addTo(map);

});

export default {
  name: 'app',
  components: {
  }
}
</script>

<style>
</style>
