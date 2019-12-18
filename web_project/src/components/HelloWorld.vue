<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div>
    <div>
      <h2>Search and add a pin</h2>
      <label>
        <gmap-autocomplete
          @place_changed="setPlace">
        </gmap-autocomplete>
        <button @click="setMarker()">맛집 찾기!</button>
      </label>
      <br/>
    </div>
    <br>
    <gmap-map :center="center" :zoom="10" style="width:100%;  height: 600px;">
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
  data() {
    return {
      msg: '19-2-oss',
      data: [],
      center: { lat: 37.1728, lng: 127.032 },
      markers: [],
      places: [],
      currentPlace: {lat: 37.1728, lng: 127.032}
    }
  },
  mounted: async function () {
    this.geolocate()
    this.setMarker()
    this.test()
  },
  firestore () {
    return {
      data: db.collection('data')
    }
  },
  methods: {
    test () {
      console.log('testsetewtasojtoiawjrfojghseawoij3rpfwbersojaw23rfweoprsbeaqfwers')
    },
    setPlace (place) {
      this.currentPlace = place
    },
    addMarker () {
      console.log("hrere")
      if (this.currentPlace) {
        console.log(this.currentPlace)
        console.log('111')
        console.log(this.currentPlace.geometry.location.lat())
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
    },
    setMarker () {
      console.log(this.data.length)
      for(var i=0;i<this.data.length;i++)
      {
        const marker = {
          lat: parseFloat(this.data[i].latitude),
          lng: parseFloat(this.data[i].longitude)
        }
        this.markers.push({ position: marker })
        //this.center = marker
      }
    }
  }
}
/*export default {
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
    //this.geolocate()
    console.log(this.test)
    this.$parent.test()
  },
  firestore () {
    return {
      data: db.collection('data')
    }
  },
  method: {
    test () {
      console.log('testsetewtasojtoiawjrfojghseawoij3rpfwbersojaw23rfweoprsbeaqfwers')
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
}*/
</script>
