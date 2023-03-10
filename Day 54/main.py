import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
  def time():
    start = time.time()
    result = function()
    end = time.time()-start
    print(f"{function.__name__} run speed: {end}s")
    return result
  return time


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i

slow_function()
fast_function()
