from elasticsearch import *


class EsQuery:
    def LocationPayload(self, es_environment, alias_lan_code, test_index, search_term, country_ctx):
        connection_es = Elasticsearch(
            [es_environment],
            http_auth=('user', 'pass'),
            port=9200, )

        result = connection_es.suggest(index="locations-" + alias_lan_code + test_index,
                                       body=dict(
                                           suggest99=dict(text=search_term, completion={"field": "suggest", "context":
                                               {"country_ctx": [country_ctx]},
                                                                                        "size": 100
                                                                                        })))
        return result
