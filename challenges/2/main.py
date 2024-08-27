def ohmsLaw(v, r, i):
    """Write your code here to calculate the missing value.

    Args:
        v (int or None): Voltage or None
        r (int or None): Resistance  or None
        i (int or None): Current  or None

    Returns: The missing value calculated to 2dp or "invalid".
    """
    # V = R * I
    # if v is missing
    my_list = [v,r,i]
    none_type = my_list.count(None)
    if none_type >= 2:
        return "Invalid"
    
    if not v:   ## if v is none
        return round(r*i,2)
    if not r:
        return round(v/i,2)
    if not i:
        return round(v/r,2)
    
    

         

