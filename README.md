# DisasterMonitor

Started only as a basic Natural Language Processing Model to identify Disaster related tweets, it turned into a full out Integrated System consisting of

1. Android Application, integrated with Machine learning API to record only Disaster related entries (Eliminating: Non Disaster Related Inputs + Metaphorical use of Disaster Words) & also view nearby anomalies.

2. A Website hosted on Gcloud, used to access all Disaster Affected Regions with GMaps and Street View (Eliminating: Fake Disaster Entries By grouping Entries in a particular GEO radius (200-300 Meters) & showing them only when a threshold is achieved (3 for Now)).

3. Custom RESTAPI (with 5 Endpoints) deployed on Cloud for Managing data across the System.
