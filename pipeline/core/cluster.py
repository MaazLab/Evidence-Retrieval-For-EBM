import requests

def lingo(docs):
    # Set the URL of the Carrot2 REST API
    url = 'http://localhost:8080/service/cluster'

    data = {'documents' : [{'abstract': doc} for doc in docs],
            "algorithm": 'Lingo', "language": 'English'}
    response = requests.post(url, json=data)
    # print(response.status_code)
    # print(response.text)
    # Parse the response JSON and print the resulting clusters
    clusters = response.json()['clusters']
    # print("clusters[0] \n",clusters[0])
    max_docs = 0
    max_docs_cluster = 0
    for i in clusters:
        total_docs = len(i['documents'])
        if total_docs > max_docs:
            max_docs = total_docs
            max_docs_cluster = i

    # print("max_docs ",max_docs)
    return [data['documents'][k]['abstract'] for k in max_docs_cluster['documents']]
