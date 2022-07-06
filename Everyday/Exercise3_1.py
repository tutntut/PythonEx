def run_timing():
    runtime = 0
    num = 0
    avg_runtime = 0
    
    while True:
        one_run = input("Enter 10 km run time : ")
        
        if one_run == '':
            avg_runtime = runtime / num
            print("Average of {:.2f} , over {} runs".format(avg_runtime, num))
            break
        else:
            num += 1
            runtime += int(one_run)
            continue


run_timing()
            
            