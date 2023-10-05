# DisasterMonitor

[Website:](http://www.disastermonitor.live/)

Started only as a basic Natural Language Processing Model to identify Disaster related tweets,  it turned into a full out Integrated System consisting of

1. Android Application,  integrated with Machine learning API to record only Disaster related entries (Eliminating: Non Disaster Related Inputs + Metaphorical use of Disaster Words) & also view nearby anomalies.

2. A Website hosted on Gcloud,  used to access all Disaster Affected Regions with GMaps and Street View (Eliminating: Fake Disaster Entries By grouping Entries in a particular GEO radius (200-300 Meters) & showing them only when a threshold is achieved (3 for Now)).

3. Custom RESTAPI (with 5 Endpoints) deployed on Cloud for Managing data across the System.

### Built Using:
GoogleCloudPlatform, NLP, MachineLearning, Flask, MYSQL, RestAPI, GoogleMapsAPI, StreetView, AndroidStudio, Java, Firebase, Volley, Python, PyMySQL, CloudComputing, Tomcat9, JSP, HTML, CSS, javascript, Jquery

https://github.com/Joyal0501/DisasterMonitor/assets/92924424/74916fe7-15b0-4c5b-ae08-6400f7695f49

