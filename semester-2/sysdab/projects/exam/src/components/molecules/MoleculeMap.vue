<template>
  <div
    id="map"
    ref="map"
  ></div>
</template>

<script>
// FIXME: Technically not an atom, i think....
import Feature from "ol/Feature";
import Geolocation from "ol/Geolocation";
import Map from "ol/Map";
import Point from "ol/geom/Point";
import View from "ol/View";
import { getTopLeft, getBottomRight } from 'ol/extent';
import { Circle as CircleStyle, Fill, Icon, Stroke, Style } from "ol/style";
import { OSM, Vector as VectorSource } from "ol/source";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import Select from 'ol/interaction/Select';
import { click } from 'ol/events/condition';

export default {
  name: "MoleculeMap",
  data() {
    return {
      view: null,
      map: null,
      geolocation: null,
      features: {
          accuracyFeature: null,
          positionFeature: null,
      },
      layers: {
        geoLayer: null,
        markerLayer: null,
      },
      oldPos: null,
      interactions: {
        click: null
      }
    };
  },
  mounted() {
    this.configureView();
    this.configureMap();
    this.configureGeoLocation();
    this.configureFeatures();
    this.configureLayers();
    this.configureClick();
 },
  methods: {
    configureView() {
      this.view = new View({
        center: [0, 0],
        zoom: 2,
      });
    },
    configureMap() {
      this.map = new Map({
        layers: [
          new TileLayer({
            source: new OSM(),
          }),
        ],
        target: this.$refs["map"],
        view: this.view,
        controls: []
      });
    },
    configureGeoLocation() {
      this.geolocation = new Geolocation({
        trackingOptions: {
          enableHighAccuracy: true,
        },
        projection: this.view.getProjection(),
      });
      
      this.geolocation.on("change:position", this.geoCallback);
      this.geolocation.setTracking(true);
    },
    configureFeatures() {
      this.features.accuracyFeature = new Feature();

      this.features.positionFeature = new Feature();
      this.features.positionFeature.setStyle(
        new Style({
          image: new CircleStyle({
            radius: 12,
            fill: new Fill({
              color: "#3399CC",
            }),
            stroke: new Stroke({
              color: "#fff",
              width: 2,
            }),
          }),
        })
      );
    },
    configureLayers() {
      this.layers.geoLayer = new VectorLayer({
        map: this.map,
        source: new VectorSource({
          features: [this.features.accuracyFeature, this.features.positionFeature],
        }),
      });

      this.layers.markerLayer = new VectorLayer({
        map: this.map,
        source: new VectorSource({
          features:[] 
        })
      })
    },
    configureClick() {
      this.interactions.click = new Select({
        condition: click
      });
      this.map.addInteraction(this.interactions.click);
      this.interactions.click.on('select', this.clickCallback); 
    },
    clickCallback(e) {
      if (e.selected.length < 0) return;
      
      let id = e.selected[0].get('bikeId');

      if (!id) return;

      let bike = this.$store.getters.getBikeById(id);
      bike.setDistance(this.calcDistance(bike.position, this.oldPos));
      
      this.$router.push({
        name: 'Cykel info',
        params: {
          bikeId: id
        }
      });
    },
    geoCallback() {
        if (this.$refs['map'] == undefined) {
          return; // Fixes an error while mounting
        }

        let coordinates = this.geolocation.getPosition();
        this.features.positionFeature.setGeometry(coordinates ? new Point(coordinates) : null);
        
        if (this.oldPos == null) {
          this.view.centerOn(coordinates, this.map.getSize(), [this.$refs['map'].offsetWidth / 2, this.$refs['map'].offsetHeight / 2]);
          this.view.setZoom(15);
        }

        // If the person has moved 20 meters, gen new points
        if (this.oldPos == null && this.$store.state.bikes && this.$store.state.bikes.length > 0) {
          this.configureMarkers(this.$store.state.bikes);
        } else if (this.oldPos == null || this.calcDistance(this.oldPos, coordinates) > 20) {
          this.generateMarkers();
        }

        this.oldPos = coordinates;
    },
    generateMarkers() {
      let extent = this.view.calculateExtent();
      let min = getTopLeft(extent);
      let max = getBottomRight(extent);
      
      let oldId = this.$store.getters.getLargestId;
      this.$store.dispatch({
        type: 'createBikes', 
        amount: 15, 
        min: min, 
        max: max
      }).then(() => {
        this.configureMarkers(this.$store.getters.getBikesOverId(oldId));
      })
   },
    configureMarkers(bikes) {
      let markerStyle = new Style({
        image: new Icon({
          opacity: 1,
          src: './bikeMarker.svg', // Uses the one from the /public dir,
          scale: 0.7
        }) 
      });
      
      let markers = [];
      for (let i = 0; i < bikes.length; i++) {
        let marker = new Feature({
          bikeId: bikes[i].id
        });
        marker.setStyle(markerStyle);
        marker.setGeometry(new Point(bikes[i].position));

        markers.push(marker)
      }

      this.layers.markerLayer.getSource().addFeatures(markers);
    },
    calcDistance(first, second) {
      return Math.sqrt(
        Math.pow(second[0] - first[0], 2) + 
        Math.pow(second[1] - first[1], 2)
      );
    }
  }
};
</script>
