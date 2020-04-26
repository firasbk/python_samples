import time as t
import matplotlib.pyplot as plt

current_time = t.localtime()
print ("the time now is: ", current_time )
print (" -------------- ")
print ("Transaction completed at : ", str(current_time.tm_hour) + "h" + str(current_time.tm_min) + "m" )

time_now = t.time()
delivery_time = time_now + (86400 * 7)
print("delivery will be on: ", t.localtime(delivery_time))

print("This program helps you type faster. Please type the word communication 5 times ")
input("Please enter to start ")

mistakes = 0
record_times = []
for i in range(0,5):
    time_now = t.time()
    word = input("Please type the word ")
    time_after = t.time()
    time_diff = round( time_after - time_now, 2 )
    record_times.append(time_diff)
    print("It took you ",time_diff, " seconds")
    if ( word.lower() != "communication"):
        mistakes += 1

print("You made ",mistakes, " mistakes")
print("now let us see your results ")
t.sleep(3)
x=[1,2,3,4,5]
plt.bar(x, record_times)

legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.ylabel('time in seconds')
plt.xlabel('Attempts')
plt.title('Your type evolution')
plt.show()


