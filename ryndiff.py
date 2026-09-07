class RynDiff:
    def __init__(self):
        self.threshold = 0.6
    
    def levenshtein(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein(s2, s1)
        if len(s2) == 0:
            return len(s1)
        
        previous_row = list(range(len(s2) + 1))
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    def damerau_levenshtein(self, s1, s2):
        len1, len2 = len(s1), len(s2)
        d = {}
        
        for i in range(-1, len1):
            d[i, -1] = i + 1
        for j in range(-1, len2):
            d[-1, j] = j + 1
        
        for i in range(len1):
            for j in range(len2):
                cost = 0 if s1[i] == s2[j] else 1
                d[i, j] = min(
                    d[i-1, j] + 1,
                    d[i, j-1] + 1,
                    d[i-1, j-1] + cost
                )
                
                if i > 0 and j > 0 and s1[i] == s2[j-1] and s1[i-1] == s2[j]:
                    d[i, j] = min(d[i, j], d[i-2, j-2] + cost)
        
        return d[len1-1, len2-1]
    
    def match(self, s1, s2):
        if not s1 or not s2:
            return 0
        
        distance = self.damerau_levenshtein(s1, s2)
        max_len = max(len(s1), len(s2))
        similarity = max(0, 1 - (distance / max_len))
        
        return similarity
    
    class diff:
        def __init__(self, parent):
            self.parent = parent
        
        def linear(self, typo, candidates, threshold=0.6):
            best_score = 0
            for candidate in candidates:
                score = self.parent.match(typo, candidate)
                if score > best_score:
                    best_score = score
            
            if best_score >= threshold:
                return True
            return False
        
        def fuzzy(self, typo, candidates, threshold=0.6):
            best_match = None
            best_score = 0
            
            for candidate in candidates:
                score = self.parent.match(typo, candidate)
                if score > best_score:
                    best_score = score
                    best_match = candidate
            
            if best_score >= threshold:
                return best_match, best_score
            return None