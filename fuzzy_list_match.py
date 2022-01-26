# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 18:49:41 2022

@author: Lucas Müller
"""

from thefuzz import fuzz
from thefuzz import process

name_list = ["John Doe", "Jane Doenna", "Kirk Stewart", "Mark Spyder"]
name_list_2 = ["Jaene Doenna", "Doe John", "Jonhy B Bad", "Kirc Steward", "Mark Spyderbanana", "Orange123"]

def fuzzy_match_lists(list_1, list_2, cutoff = 0, partial_match = True, ignore_repetitions = True, ignore_order = True):
    """
    Goal
    ----------
    Given 2 list of unordered strings, iterates through every list_1 element and 
    looks up in list_2 for simmilar strings. It uses multiple algorithms to evaluate string simmilarity,
    including the posibility to account for word arrangement, partial matches  and repetitions.
    Returns a list of tuples with the best possible match of every list_1 element, and a score from
    0 to 100 being 100 a perfect match.   
    
    Parameters
    ----------
    - list_1 : A list of strings to iterate. Can be any size.
    - list_2 : A second list of strings to lookup for similar strings while iterating list_1.
    - cutoff : optional. Int 0-100, default is 0. A string with the best match score lesser than 
      the cutoff will not be returned. When cutoff = 0, the algorithm will always return a match 
      for every list_1 string, even when it's clearly incorrect..
    - partial_match: optional. When true, partial matches don't reduce score (e.g: "John Doe" == "John Doe Jr.")
    - ignore_repetitions: optional. When true, word repetition don't reduce score (e.g: "John John Doe" == "John Doe")'
    - ignore_order: optional. When true, word arrangement don't reduce score (e.g: "John Doe" == "Doe John")
    
    Returns
    -------
    matches : List of tuples [(string list_1 original, string list_2_match, int score 0-100)]
    """

    matches = []
    for name in list_1:
        # Iterates every list_1 element and uses thefuzz to get the best match possible from list_2
        fuzz_match = []
        
        #Simple comparison
        fuzz_match.append(process.extractOne(name, list_2, scorer = fuzz.ratio)) 
        #Partial comparison
        if partial_match: 
            fuzz_match.append(process.extractOne(name, list_2, scorer = fuzz.partial_ratio))
        #Repetition comparison
        if ignore_repetitions:
            fuzz_match.append(process.extractOne(name, list_2, scorer = fuzz.token_set_ratio))
        #Orderless comparison
        if ignore_order:
            fuzz_match.append(process.extractOne(name, list_2, scorer = fuzz.token_sort_ratio))
            
        scores = [x[1] for x in fuzz_match] # List of scores for every algorithm tried
        best_match = fuzz_match[scores.index(max(scores))] 
        
        if best_match[1] > cutoff: # Cutoff can be defined to give up if the match isn't good enough
          matches.append((name, best_match[0], best_match[1]))
      
    return matches

test = fuzzy_match_lists(name_list, name_list_2)
