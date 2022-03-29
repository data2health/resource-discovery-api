# Resource Discovery API

## Data Tracking
Tracking notes for updates to the data used in the API.


- Added aliases for the newly cloned outbreak indices. *3.14.2022*
 

- Added `resourceTypeName` field and update `author.name` and `author.name.affiliation` field for aggregation in outbreak indices. *3.10.2022*



<details>
<summary>Currently Updated Fields</summary>


```
GET http://search.cd2h.org:9200/outbreak_litcovid_202110070745_vvrw8kmo/_mapping/field/author.affiliation.name,author.name
{
    "outbreak_litcovid_202110070745_vvrw8kmo": {
        "mappings": {
            "author.name": {
                "full_name": "author.name",
                "mapping": {
                    "name": {
                        "type": "text",
                        "copy_to": [
                            "all"
                        ]
                    }
                }
            },
            "author.affiliation.name": {
                "full_name": "author.affiliation.name",
                "mapping": {
                    "name": {
                        "type": "keyword",
                        "copy_to": [
                            "all"
                        ]
                    }
                }
            }
        }
    }
}
```  

</details>

## API Updates  
- added `post_filter` 