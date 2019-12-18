<template>
  <div class="hello">
    <h1>{{data}}</h1>
    <h1>{{ msg }}</h1>
    <div>
    <div>
      <h2>Search and add a pin</h2>
      <label>
        <gmap-autocomplete
          @place_changed="setPlace()">
        </gmap-autocomplete>
        <button @click="addMarker()">Add</button>
      </label>
      <br/>

    </div>
    <br>
    <gmap-map :center="center" :zoom="15" style="width:100%;  height: 600px;">
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        @click="center=m.position"
      ></gmap-marker>
    </gmap-map>
  </div>
  </div>
</template>

<script>
import { db } from '../main'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: '19-2-oss',
      data: [],
      center: { lat: 37.1728, lng: 127.032 },
      markers: [],
      places: [],
      currentPlace: {lat: 37.1728, lng: 127.032}
    }
  },
  mounted () {
    this.geolocate()
    this.test()
  },
  firestore () {
    return {
      data: db.collection('data')
    }
  },
  method: {
    test () {
      console.log('test')
    },
    setPlace (place) {
      this.currentPlace = place
    },
    addMarker () {
      if (this.currentPlace) {
        console.log('111')
        const marker = {
          lat: this.currentPlace.geometry.location.lat(),
          lng: this.currentPlace.geometry.location.lng()
        }
        this.markers.push({ position: marker })
        this.places.push(this.currentPlace)
        this.center = marker
        this.currentPlace = null
      }
    },
    geolocate: function () {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        }
      })
    }
  }
}
</script>
