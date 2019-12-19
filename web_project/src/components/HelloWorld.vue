<template>
  <div>
    <h1>{{ msg }}</h1>
    <div>
      <label>
        <!--gmap-autocomplete
          @place_changed="setPlace">
        </gmap-autocomplete-->
      </label>
      <v-select v-model="selectedSi" :options="sis" placeholder="찾을 시를 선택하세요" class="form-control">
      </v-select>
       <v-btn @click="setMarker()">
          검색
        </v-btn>
      <br/>
    <br>
    <gmap-map :center="center" :zoom="13" style="width:100%;  height: 600px;">
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        @click="toggleInfoWindow(m,index)"
        @mouseover="toggleInfoWindow(m,index)"
      ></gmap-marker>

      <gmap-info-window
        :options="infoOptions"
        :position="infoWindowPos"
        :opened="infoWinOpen"
        @closeclick="infoWinOpen=false"
      >
      <div v-html="infoContent"></div>
    </gmap-info-window>
    </gmap-map>
  </div>
  </div>
</template>

<script>
import { db } from '../main'
export default {
  data () {
    return {
      selectedSi: '',
      sis: ['가평군', '고양시', '과천시', '광주시', '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시',
        '여주시', '연천군', '오산시', '용인시', '의왕시', '의정부시', '이천시', '평택시', '파주시', '포천시', '하남시', '화성시'],
      msg: '19-2-oss',
      data: [],
      center: { lat: 37.1728, lng: 127.032 },
      markers: [],
      places: [],
      currentPlace: {lat: 37.1728, lng: 127.032},
      map: null,
      infoContent: '',
      infoWindowPos: {
        lat: 0,
        lng: 0
      },
      infoWinOpen: false,
      currentMidx: null,
      infoOptions: {
        pixelOffset: {
          width: 0,
          height: -35
        }
      }
    }
  },
  mounted: async function () {
    this.geolocate()
    this.setMarker()
  },
  firestore () {
    return {
      data: db.collection('data')
    }
  },
  methods: {
    setPlace (place) {
      this.currentPlace = place
    },
    addMarker () {
      if (this.currentPlace) {
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
      this.markers = []
      for (var i = 0; i < this.data.length; i++) {
        if (this.data[i].si === this.selectedSi) {
          const marker = {
            lat: parseFloat(this.data[i].latitude),
            lng: parseFloat(this.data[i].longitude)
          }
          this.markers.push({
            name: this.data[i].storename,
            position: marker,
            si: this.data[i].si,
            telno: this.data[i].telno,
            address: this.data[i].address,
            star: this.data[i].score,
            menu: this.data[i].menu
          })
          this.center = marker
        }
      }
    },
    toggleInfoWindow: function (marker, idx) {
      this.infoWindowPos = marker.position
      this.infoContent = this.getInfoWindowContent(marker)
      if (this.currentMidx === idx) this.infoWinOpen = !this.infoWinOpen
      else {
        this.infoWinOpen = true
        this.currentMidx = idx
      }
    },

    getInfoWindowContent: function (marker) {
      return (`<div class="card">
        <div class="card-content">
        <div class="media">
        <div class="media-content">
        <p class="title is-6">음식점 이름 : ${marker.name}</p>
        <p class="title is-4">대표 메뉴 : ${marker.menu}</p>
        <p class="title is-4">전화번호 : ${marker.telno}</p>
        <p class="title is-4">주소 : ${marker.address}</p>
        <p v-if="market.star" class="title is-4">점수 : ${marker.star}</p>
        </div>
        </div>
        </div>
        </div>`)
    }
  }
}
</script>
<style>
body {
  font-family: sans-serif;
  margin: 42px;
}

.tooltip {
  display: block !important;
  z-index: 10000;
}

.tooltip .tooltip-inner {
  background: black;
  color: white;
  border-radius: 16px;
  padding: 5px 10px 4px;
}

.tooltip .tooltip-arrow {
  width: 0;
  height: 0;
  border-style: solid;
  position: absolute;
  margin: 5px;
  border-color: black;
}

.tooltip[x-placement^="top"] {
  margin-bottom: 5px;
}

.tooltip[x-placement^="top"] .tooltip-arrow {
  border-width: 5px 5px 0 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  bottom: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip[x-placement^="bottom"] {
  margin-top: 5px;
}

.tooltip[x-placement^="bottom"] .tooltip-arrow {
  border-width: 0 5px 5px 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-top-color: transparent !important;
  top: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip[x-placement^="right"] {
  margin-left: 5px;
}

.tooltip[x-placement^="right"] .tooltip-arrow {
  border-width: 5px 5px 5px 0;
  border-left-color: transparent !important;
  border-top-color: transparent !important;
  border-bottom-color: transparent !important;
  left: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip[x-placement^="left"] {
  margin-right: 5px;
}

.tooltip[x-placement^="left"] .tooltip-arrow {
  border-width: 5px 0 5px 5px;
  border-top-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  right: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip[aria-hidden='true'] {
  visibility: hidden;
  opacity: 0;
  transition: opacity .15s, visibility .15s;
}

.tooltip[aria-hidden='false'] {
  visibility: visible;
  opacity: 1;
  transition: opacity .15s;
}
</style>
