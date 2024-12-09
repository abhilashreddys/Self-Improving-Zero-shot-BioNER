from scipy import stats

def should_stop_ner(observations, threshold):
    """
    Beta stopping criteria adapted for NER
    """
    # Group by entity spans
    entity_groups = {}
    for pred in observations:
        for entity in pred:
            span = (entity['start'], entity['end'])
            label = entity['label']
            key = (span, label)
            if key not in entity_groups:
                entity_groups[key] = 0
            entity_groups[key] += 1
    
    total_samples = len(observations)
    
    # For each unique entity span+label combination
    for key, count in entity_groups.items():
        # Find second most common prediction for this span
        v1 = count  # Count of most common label
        v2 = max([c for k,c in entity_groups.items() 
                  if k[0] == key[0] and k != key] or [0])  # Count of second most common
                  
        # Calculate beta distribution probability
        prob = compute_beta_probability(v1, v2, total_samples)
        
        if prob < threshold:
            return False
            
    return True

def compute_beta_probability(v1, v2, n):
    """
    Compute probability using beta distribution
    """
       
    # Parameters for beta distribution
    a = v1 + 1
    b = v2 + 1
    
    # Probability that p1 > p2
    return 1 - stats.beta.cdf(0.5, a, b)

def get_majority_entities(observations):
    """
    Get majority vote for each entity span
    """
    entity_counts = {}
    for pred in observations:
        for entity in pred:
            span = (entity['start'], entity['end'])
            label = entity['label']
            key = (span, label)
            entity_counts[key] = entity_counts.get(key, 0) + 1
            
    # Get majority entities above threshold
    n = len(observations)
    majority_entities = [
        {'span': k[0], 'label': k[1], 'count': v}
        for k, v in entity_counts.items()
        if v/n > 0.5
    ]
    return majority_entities