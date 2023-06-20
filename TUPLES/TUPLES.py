

#alist name etc
alist = ["st1ko", "hackwell", 92]

#change the alist name with the index so index 0 is st1ko, but [0] = zenuu so it changes the name 
alist [0] = "zenuu"

print (alist)

atuple = ["st1ko", "hackwell", 92]

atuple [0] = "zenuu"

print (atuple)

# tuples is much faster, so to prove it we are going to do a test 

#list speed test
import timeit

print(timeit.timeit(stmt='["red", "blue", "green", 5, 7, 12, 18, "dude"]', nummber=10000000))


#tuple speed test

print(timeit.timeit(stmt='("red", "blue", "green", 5, 7, 12, 18, "dude")', nummber=10000000))






