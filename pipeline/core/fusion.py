

def process_results(dict,weight):
    # Normalizing the results
    min_val = min(dict.values())
    max_val = max(dict.values())
    
    print('min_val ',min_val)
    print('max_val ',max_val)

    # Apply weightage to result  
    normalized_dict = {key:((dict[key] - min_val) / (max_val - min_val))*weight for key in dict}
    
    return normalized_dict

def fusing_results(ppr_score,auth_score,rel_score):

    ppr_score = process_results(ppr_score,.15)
    auth_score = process_results(auth_score,.15)
    rel_score = process_results(rel_score,.7)

    fused_result = {key : (ppr_score[key]+auth_score[key]+rel_score[key])/3 for key in ppr_score.keys()}
    return fused_result