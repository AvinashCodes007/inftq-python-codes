def solve(head,legs):
    error_msg="no solution"
    chicken_count=0
    rabbit_count=0
    if (legs/2!=0 and head>legs):
        print(error_msg)
    rabbit_count=(legs-2*(head))//2
    chicken_count=(head)-(legs - 2*(head))//2
    return rabbit_count,chicken_count
print(solve(3,6))