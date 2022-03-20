def check_food_id(food_times, k):
    remain_food_amt = food_times.copy()
    cur_food_id = 1
    
    for ts in range(1, k+1):
        
        #----- 01: check if remain food amt is not 0
        if all([amt<=0 for amt in remain_food_amt]):
            cur_food_id = -1
            return cur_food_id
        
        #----- 02: found remain food & update food id
        while True:
            
            if remain_food_amt[cur_food_id-1] > 0:
                break
                
            else:
                cur_food_id = (cur_food_id + 1) % len(remain_food_amt)          
            
        #----- 03: update remain food
        remain_food_amt[cur_food_id-1] += -1
    
    cur_food_id = (cur_food_id + 1) % len(remain_food_amt)
    
    return cur_food_id