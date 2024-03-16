from core import database as db

def evaluate_quality(doc_list):
    metadata = db.find_from_abstract(doc_list)
    ppr_evaluation = evaluate_paper(metadata)
    auth_evaluation = evaluate_author(metadata)
    return ppr_evaluation, auth_evaluation

def evaluate_paper(doc_list):
    sjr_quartile_mapper = {"Q1":3,
                            "Q2":2,
                            "Q3":1,
                            "Q4":0}
    evaluation_result = {}
    for doc in doc_list:
        evaluation_result.update({doc['abstract'] : doc['h_index']+doc['citations']+doc['sjr_rank']+sjr_quartile_mapper[doc['sjr_quartile']]})
    return evaluation_result

def evaluate_author(doc_list):
    evaluation_result = {}
    for doc in doc_list:
        evaluation_result.update({doc['abstract'] : doc['author_citations']+doc['author_h_index']})
    return evaluation_result

