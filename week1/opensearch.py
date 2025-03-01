from flask import g, current_app
from opensearchpy import OpenSearch


def get_opensearch():
    host = 'localhost'
    port = 9200
    auth = ('admin', 'admin')
    
    return OpenSearch(
        hosts=[{'host': host, 'port': port}], 
        http_auth=auth,
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
        timeout=60,
        )


def create_index(index_name, index_body):
    client = get_opensearch()
    
    if client.indices.exists(index_name):
        client.indices.delete(index_name)
    
    return client.indices.create(index_name, index_body)
