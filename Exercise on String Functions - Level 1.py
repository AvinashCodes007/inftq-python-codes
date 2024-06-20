def count_name(name_list):
    count=0
    error_count=0
    for i in name_list:
        if i.endswith('at'): # we will handle count in this case only
            count += 1
        if 'at' in i :    # isme apan ko in ya find lagakar err_count calculate karna hai, jisme end, start, middle k sab cases include ho jaate h automatically iss method se
            error_count+=1
        
    print("_at ->",count)
    print("%at%" ,error_count)
        
name_list=["Hat","Cat","rabbit","matter"]  
count_name(name_list)

    

