from core import retrieval, cluster, evidence, quality, fusion


query = input("Enter Query: ")

rel_docs_score = retrieval.retrieve_docs(query, k=50)
# print(relevant_docs)
# for relevant_doc in relevant_docs:
#     print(relevant_doc)
#     print('==================================')
cluster_docs = cluster.lingo(docs=rel_docs_score.keys())
# print("cluster_docs \n",cluster_docs[0])
# print(len(cluster_docs))

ppr_score, auth_score = quality.evaluate_quality(cluster_docs)

fused_result = fusion.fusing_results(ppr_score, auth_score, rel_docs_score)

evidence_list = evidence.get_pico(fused_result)
print(evidence_list[0])



if __name__ == '__main__':
    pass