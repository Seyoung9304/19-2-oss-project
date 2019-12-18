// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { firestorePlugin } from 'vuefire'
import firebase from 'firebase/app'
import 'firebase/firestore'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBWfBpAVmaw98fBmVWRVzdNumZXrEZ0qNM',
    libraries: 'places'
  }
})

Vue.use(firestorePlugin)
var firebaseConfig = {
  apiKey: 'AIzaSyBp9qZ87OMBpMgsql2Ty4bYY9HlyHOmPk0',
  authDomain: 'oss-d85b6.firebaseapp.com',
  databaseURL: 'https://oss-d85b6.firebaseio.com',
  projectId: 'oss-d85b6',
  storageBucket: 'oss-d85b6.appspot.com',
  messagingSenderId: '177361667729',
  appId: '1:177361667729:web:d51c9f369f1afed5eb6130',
  measurementId: 'G-5BGT9PMBCZ'
}
firebase.initializeApp(firebaseConfig)
export const db = firebase.firestore()
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
