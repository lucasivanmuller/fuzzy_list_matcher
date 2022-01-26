    Goal
    ----------
    Given 2 list of unordered strings, iterates through every list_1 element and 
    looks up in list_2 for simmilar strings. It uses multiple algorithms to evaluate string simmilarity,
    including the posibility to account for word arrangement, partial matches  and repetitions.
    Returns a list of tuples with the best possible match of every list_1 element, and a score from
    0 to 100 being 100 a perfect match.   
    
    Use case
    --------
    You have a list of manually typed data (e.g. list of names) with small mistakes (transcription error, OCR error, transposition, etc) and have to look up in a register
    for the corresponding element.
    
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

